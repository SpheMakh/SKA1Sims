#!/usr/bin/env python
import numpy
import math
import re
import sys

stats_file = sys.argv[1]
format = "%(lo0)s %(lores)s %(lofreq)d %(freq)d %(dec)d  %(weight)s %(widx)d " + \
  "%(noise166).2g  %(noise50).2g %(psf_sym).2f %(psf_ex).2g %(psf_ey).2g %(psf_mean).2g %(noise50k).2g %(sdl).2g\n";

# determine field names from format string
fields = [ x.split(")")[0] for x in format.split("(")[1:] ];

ff = file("%s.txt"%(stats_file[:-3]),"w");
ff.write("# "+" ".join(fields)+"\n");
ff1 = file("%s.csv"%(stats_file[:-3]),"w");
ff1.write(",".join(fields)+"\n");

execfile(stats_file)
genstats = noisestats

resbins = set()
wbins = set()

def reprocess_dict (dict1):
  """reprocess the dict for convenience"""
  out = {};
  for kk,value in dict1.iteritems():
    # parse keys
    (lo0,dur,decdec,freqmhz,nch),weight = kk[0].split("_"),kk[1]
    if weight != "natural":
      weight += ":" + kk[3];
    dec = -int(decdec.split("-")[1]);
    freq = int(freqmhz[:-3])
    # parse layout
    lo = lo0;
    if lo[-2] in "abcd":
      lores = "0."+lo[-1];
      lofreq = dict(a=650,b=800,c=1000,d=1400)[lo[-2]];
      lo = lo[:-2];
    else:
      lores = 0;
      lofreq = 0;
    lo = lo[4:];
    l00 = lo0[4:]
    wbins.add(weight);
    # make new entry
    out[lo0,lores,lofreq,freq,dec,weight] = [value,kk];
  return out;

PIXNOISE = reprocess_dict(genstats['pixnoise']);
PSF_FWHM = reprocess_dict(genstats['psf_fwhm']);
SIDELOBES = reprocess_dict(genstats['sidelobes']);
wbins = sorted(wbins);

for kk,(noise50,origkey) in PIXNOISE.items():
  lo0,lores,lofreq,freq,dec,weight = kk
  ex,ey,mean = PSF_FWHM[lo0,lores,lofreq,freq,dec,weight][0][:3]
  # PSF metrics
  psf_area = numpy.pi*(ex*ey)
  exey = sorted([ex,ey])
  psf_sym = 1.0 - exey[0]/exey[1]
  psf_mean = mean
  psf_ex,psf_ey = ex,ey
  try :sdl = SIDELOBES[lo0,lores,lofreq,freq,dec,weight][0][0] *1e3
  except TypeError : sdl = SIDELOBES[lo0,lores,lofreq,freq,dec,weight][0] *1e3
  noise50 *= 1e6
  noise166 = noise = noise50/math.sqrt(166./50) 
  noise50k = noise50/math.sqrt(50e-3/50)
  widx = wbins.index(weight) 
  ff.write(format%locals());
  ff1.write(format.replace(" ",",")%locals());
