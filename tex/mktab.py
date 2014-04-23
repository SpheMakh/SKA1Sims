#!/usr/bin/python
import numpy
import math
import re
import sys

stats_file = sys.argv[1]
format = "%(lo0)s %(lores)s %(lofreq)d %(freq)d %(dec)d %(resbin)s %(ridx)d %(weight)s %(widx)d " + \
  "%(noise166).2g %(flux10).2f %(snr10).2f %(hours).2f %(snravg).2f %(relnoise).2f %(noise50).2g %(noise50_ref2).2g  %(psf_area).2g %(psf_sym).2f %(psf_mean).4f %(noise50k).2g %(speed).2g %(speed_avg).2g\n";

# determine field names from format string
fields = [ x.split(")")[0] for x in format.split("(")[1:] ];

ff = file("%s.txt"%(stats_file[:-3]),"w");
ff.write("# "+" ".join(fields)+"\n");
ff1 = file("%s.csv"%(stats_file[:-3]),"w");
ff1.write(",".join(fields)+"\n");

execfile(stats_file)
#import genstats
genstats = noisestats
mss = mss = genstats['pixnoise0'].keys()

resbins = set()
wbins = set()

def reprocess_dict (dict1):
  """reprocess the dict for convenience"""
  out = {};
  for kk,value in dict1.iteritems():
    # parse keys
    lo0,dur,decdec,freqmhz,nch = kk[0].split("_");
    r0,r1 = float(kk[1]),float(kk[2]);
    weight = kk[3];
    if weight != "natural":
      weight += ":" + kk[5];
    dec = -int(decdec.split("-")[1]);
    freq = int(freqmhz[:-3])
    # parse layout
    lo = lo0;
    if lo[-2] in "abc":
      lores = "0."+lo[-1];
      lofreq = dict(a=650,b=800,c=1000)[lo[-2]];
      lo = lo[:-2];
    else:
      lores = 0;
      lofreq = 0;
    lo = lo[4:];
    l00 = lo0[4:]
    resbins.add((r0,r1));
    wbins.add(weight);
    # make new entry
    out[lo0,lores,lofreq,freq,r0,r1,dec,weight] = [value,kk];
  return out;

PIXNOISE = reprocess_dict(genstats['pixnoise']);
PSF_FWHM = reprocess_dict(genstats['psf_fwhm']);
resbins = sorted(resbins);
wbins = sorted(wbins);

# discard layouts where bin 0 (0.4"-1") is unpopulated because it's been scaled out
# due to a bug in the imager, these will actually have ALL uv-points in them and the 
# noise is therefore meaningless -- they can nonetheless be identified by naturally-weighted 
# psf_fwhm being >1"
for kk,(noise,origkey) in PIXNOISE.items():
  lo0,lores,lofreq,freq,r0,r1,dec,weight = kk;
  # is first resolution bin?
  if resbins.index((r0,r1)) == 0:
    fwhm = PSF_FWHM[tuple(list(kk)[:-1]+["natural"])][0];
    if (fwhm[0] > 1 and fwhm[1] > 1) or not fwhm[0] or not fwhm[1]:
      print "blanking",kk,": scaled out (%f %f %f)"%(fwhm[0],fwhm[1],PIXNOISE[kk][0]);
      PIXNOISE[kk][0] = 0;

# now process again and derive some values
for kk,(noise50,origkey) in PIXNOISE.items():
  lo0,lores,lofreq,freq,r0,r1,dec,weight = kk;
  # get psf stats
  ex,ey,mean = PSF_FWHM[lo0,lores,lofreq,freq,r0,r1,dec,weight][0][:3]
  # look up noise for SKA1REF2 as reference value
  noise50 *= 1e+6;
  noise50_ref2 = PIXNOISE[tuple(["SKA1REF2",0,0]+list(kk)[3:])][0]*1e+6;
  noise166 = noise = noise50/math.sqrt(166./50.);
  noise50k = noise50/math.sqrt(50e-3/50.)
  relnoise = noise50/noise50_ref2;
  # look up resolution and weight bin
  ridx = resbins.index((r0,r1))
  widx = wbins.index(weight);
  # compute adjusted SNR ratio (relative to 10 uJy at 1000 MHz): scale up by source flux
  flux10 = 10*(freq/1000.)**-0.7; 
  snr10 = (flux10/noise166) if noise166 else 0;
  # compute the normalized SNR as follows:
  # assume flux=10uJy at 1000, rescale with spectral index
  snr1 = numpy.zeros(3,float)
  speed_freq = numpy.zeros(3,float)
  for i,freq1 in enumerate((650,800,1000)):
    noise1 = PIXNOISE[lo0,lores,lofreq,freq1,r0,r1,dec,weight][0]*1e+6/math.sqrt(166./50.);
    if noise1:
      # flux of 10uJy scaled to frequency, noise scaled to 166 MHz band
      snr1[i] = 10*(freq1/1000.)**-0.7 / noise1;
  # compute average survey speed
      fov_freq = 1.4 * (700./freq1)**2 if lo0.startswith('SKA1') else 18.
      speed_freq[i] = fov_freq  *  ( (10*(freq1/1000.)**-0.7) / noise1) **2
  # compute average SNR
  snravg = math.sqrt((snr1**2.).sum()/len(snr1));
  # this is the SNR after 8 hours -- how many hours needed for SNR=10?
  hours = 8*(10/snravg)**2 if snravg else 1e+99;
  speed_avg = math.sqrt((speed_freq**2).sum()/len(speed_freq))
  fov = 1.4 * (700./freq)**2 if lo0.startswith('SKA1') else 18.
  speed  = fov  *  snr10**2
  # write result
  # ----------------------------------------
  # PSF metrics
  psf_area = numpy.pi*(ex*ey)
  exey = sorted([ex,ey])
  psf_sym = 1.0 - exey[0]/exey[1]
  psf_mean = mean
  # ----------------------------------------
  resbin = "%.1f-%.1farcsec"%(r0,r1) if r0<60 else "%.1f-%.1farcmin"%(r0/60,r1/60);
  ff.write(format%locals());
  ff1.write(format.replace(" ",",")%locals());
