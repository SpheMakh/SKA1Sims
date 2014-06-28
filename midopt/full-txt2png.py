#!/usr/bin/env python
import math
import numpy as np
import pylab as plt
import os,sys


def color_legend_texts(leg):
    """Color legend texts based on color of corresponding lines"""
    for line, txt in zip(leg.get_lines(), leg.get_texts()):
        txt.set_color(line.get_color())  
_YLABELS = dict(psf_mean='PSF Size [Arcsec]',psf_sym='PSF symetry',sdl='RMS sidelobe level   $10^{-3}$ ',noise50='Noise [uJy/Beam]',noise50k='Noise [uJy/Beam]')
if __name__=='__main__':
  std = open(sys.argv[1])
  hdr = std.readline()[2:-1]
  names = hdr.split()
  dtype = ['float64']*len(names)
  dtype[0],dtype[5] = ['S50']*2
  lays,nlays = 'SKA1V8 SKA1W8-0C0B120 SKA1W8-0C9B120 SKA1W8-12C0B120 SKASUR SKASUR75'.split(),6
  decs,ndecs = '-30'.split(),1
  freqs,nfreqs = '650 800 1000 1400'.split(),4
  weights,nwi = "robust-2 weighting,natural weigthing,robust-2 weighting with a 1 arcsec Gaussian taper".split(","),3
  decsWeights = {}
  
  for d in decs:
    for j,w in enumerate(weights):
       decsWeights["%s:%d"%(d,j)] = "DEC=%s, %s"%(d,w)
  Stats = np.genfromtxt(std.readlines(),names=names,dtype=dtype)
  stats = Stats[np.argsort(Stats,order=["dec","widx","lo0","freq"])] 
  #print stats
  metrics = names[7:]
  STATS = {}
  for n in range(nlays*ndecs*nwi):
    start,end = n*nfreqs,(n+1)*nfreqs
    freq = stats[start:end]
    #print freq,start,end,freq.shape
    s = {}
    for wi in range(nwi):
      tmp = "%d:%d:%s"%(freq["widx"][0],int(freq["dec"][0]),freq['lo0'][0])
      print tmp,"\n------------------"
      for metric in metrics:
        vals = freq[metric]
        s[metric] = vals
      STATS[tmp] = s
      #print s
  print "INFO:: Making plots "
  exclude = 'noise166 psf_ex psf_ey'.split()
  for wi in [1,0,2]:
    for dec in decs:
      for metric in metrics:
	if metric not in exclude:
         print 'INFO:: Ploting %s || DEC=%s WIDX=%s'%(metric,dec,wi)
         ax1 = plt.subplot(211)
         plt.subplots_adjust(hspace=0.1)
         mn,mx = [None,None]
         for lay in 'SKASUR SKASUR75'.split():
           key = '%d:%s:%s'%(wi,dec,lay)
           data = STATS[key][metric]
           if metric.startswith('noise'): 
             if 2==1 : #wi!=0
               data *= ((STATS[key]['psf_ex']*STATS[key]['psf_ey']  *np.pi)/0.5**2)
               _YLABELS[metric] = 'Noise [Jy/Pixel]'
           if mn ==None: mn,mx = data.min(),data.max()
	   else:
             if data.min() <mn : mn = data.min()
             if data.max() >mx : mx = data.max()
           ax1.plot(range(4),data,'--',label=lay.split('SKA')[-1],ms=3)
         ax1.grid()
         ax1.set_ylim(mn*.8,mx*1.2)
         ax1.set_ylabel(_YLABELS[metric])
         leg = ax1.legend(frameon=False,prop={'size':9})
         color_legend_texts(leg)
         ax2 = plt.subplot(212,sharex=ax1)
         mn,mx = [None,None]
         for lay in 'SKA1V8 SKA1W8-0C0B120 SKA1W8-0C9B120 SKA1W8-12C0B120'.split():
           key = '%d:%s:%s'%(wi,dec,lay)
           data = STATS[key][metric]
           if mn ==None: mn,mx = data.min(),data.max()
	   else:
             if data.min() <mn : mn = data.min()
             if data.max() >mx : mx = data.max()
           ax2.plot(range(4),data,'--',label=lay.split('SKA1')[-1],ms=3)
         ax2.grid()
         ax2.set_ylim(mn*.8,mx*1.2)
         leg = ax2.legend(frameon=False,prop={'size':9})
         color_legend_texts(leg)
         xticklabels = ax1.get_xticklabels()
         ax2.set_ylabel(_YLABELS[metric])
         plt.setp(xticklabels, visible=False)
         plt.xlabel('Freq [MHz]')
         plt.xticks(range(4),freqs)
         plt.xlim(-.5,3.5)
         plt.savefig('images/%s-%d_%s.png'%(metric,wi,dec))
         plt.clf()
