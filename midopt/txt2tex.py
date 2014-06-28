#!/usr/bin/env python
import numpy as np
import sys,os
from optparse import OptionParser

CLR = "For each column the intensity of the colour increases with the value"
SUF = "These values are generated at 650, 800 and 1000 MHz, at angular scales \\{0.4-1, 0.4-2, 1-2, 2-3, 3-4, \
3-10, 10-60, 10-100, 600-3600\\} arcsec and are labelled {\\it resbin} \\{1, 2, 3, 4, 5, 6, 7, 8, 9\\} respectively. This is done for natural \
weighting at declination -30 degrees. %s."%CLR
CPT = {}
CPT["noise50k"] = "Noise (in $\\mu$Jy/Beam) for a 50kHz band after an 8hr synthesis with a 60s integration for the different layouts at different angular scales. %s"%SUF
CPT["noise50"] = "Noise (in $\\mu$Jy/Beam) for a 50MHz band after an 8hr synthesis with a 60s integration for the different \
layouts at different angular scales. %s"%SUF
CPT["noise166"] = "Noise (in $\\mu$Jy/Beam) for a 166MHz band after an 8hr synthesis with a 60s integration for \
the different layouts at different angular scales. %s"%SUF
CPT["snr10"] = "SNR after 8 hours relative to a 10$\\mu$Jy source at 1000Hz (166 MHz band) with a spectral \
 index of -0.7 for the different layouts. %s"%SUF

CPT["snravg"] = "SNR after 8 hours relative to a 10$\\mu$Jy source at 1000Hz (166 MHz band) with a spectral index of \
-0.7 averaged over 650,800 and 1000MHz, for the different layouts at different angular scales. These values are \
generated for angular scales \\{0.4-1, 0.4-2, 1-2, 2-3, 3-4, 3-10, 10-60, 10-100, 600-3600\\} arcsec and are labelled {\\it resbin} \\{1, 2, \
3, 4, 5, 6, 7, 8, 9\\} respectively. This is done for natural weighting at declination -30 degrees. %s."%CLR

CPT["hours"] = "The hours required to reach a mean SNR of 10 (average over 650,800 and 1000MHz), relative to a \
10$\\mu$Jy source at 1000MHz with a spectral index of -0.7 for the different layouts at different angular scales. These \
values are generated for angular scales \\{0.4-1, 0.4-2, 1-2, 2-3, 3-4, 3-10, 10-60, 10-100, 600-3600\\} arcsec and are labelled {\\it \
resbin} \\{1, 2, 3, 4, 5, 6, 7, 8, 9\\} respectively. This is done for natural weighting at declination -30 \
degrees. %s."%CLR


CPT["psf_sym"] = "PSF symmetry (see \\autoref{sec:exp})  for the different layouts at different angular scales. \
These values are generated at 650, 800 and 1000MHz for angular scales \\{0.4-1, 0.4-2, 1-2, 2-3, 3-4, 3-10, 10-60, 10-100, 600-3600\\} arcsec \
and are labelled {\\it resbin} \\{1, 2, 3, 4, 5, 6, 7, 8, 9\\} respectively. This is done for natural weighting at declinations \
-10, -30 and -50 degrees. %s."%CLR

CPT["psf_mean"] = "FWHM PSF sizes (in arcsec) for the different layouts at different angular scales. These values are \
generated at 650, 800 and 1000MHz for angular scales \\{0.4-1, 0.4-2, 1-2, 2-3, 3-4, 3-10, 10-60, 10-100, 600-3600\\} arcsec and are labelled \
{\\it resbin} \\{1, 2, 3, 4, 5, 6, 7, 8, 9\\} respectively. This is done for natural weighting at declination -30 \
degrees. %s."%CLR 

def select_color(c,v,color):
   fct = .6
   val = c *70 + 30
   if v<0.1 : tmp = "%.2f \\cellcolor{%s!%.2f}"%(v,color,val*fct)
   elif v<100 : tmp = "%.1f \\cellcolor{%s!%.2f}"%(v,color,val*fct)
   else : tmp = "%.4g \\cellcolor{%s!%.2f}"%(v,color,val*fct)
   return tmp

def color(data):
    new = np.ndarray([data.shape[0],data.shape[1]],dtype="S100")
    color = {'0':'blue','1':'red','2':'green','3':'orange','4':'purple','5':'blue','6':'red','7':'green','8':'orange','9':'purple'}
    for i in range(data.shape[1]):
        min,max = float(data[:,i].min()),float(data[:,i].max())
        for j in range(data.shape[0]):
            cl = (data[j,i]-min)/(max-min) if data[j,i]!=min else 0
            new[j,i] = select_color(cl,data[j,i],color[repr(i)])
    return new

def caption(metric,cpt=CPT):
  """Returns caption for a given metric"""
  return "\\caption{%s}"%(cpt[metric])
ALL_DECS = False if sys.argv[-1].startswith('dec30') else True # probalbly should use option parser for this script now
if __name__=="__main__":
  opt = OptionParser()
  opt.set_usage('%prog [options] stats_txt_file')
  opt.add_option('-l','--label',dest='label',default=None,help='Suffix to add the tex files')
  opt.add_option('-o','--oneDec',dest='oneDec',default=None,help='Get stats for these declinations. Comma seperated values')
  opt.add_option('-L','--lays',dest='lays',default='SKA1V8,SKA1W8-V2,SKA1W8,SKA1W8-C9B120,SKA1V8-C9B120,SKA1W8-12C0B120,SKASUR,SKASUR1',help='Layouts in stat file')
  opt.add_option('-D','--dlays',dest='dlays',default='SKA1V8,SKA1W8-V2,SKA1W8-C9B120,SKA1W8-12C0B120,SKASUR1,SKASUR',help='Layouts in stat file')
  opt.add_option('-S','--slays',dest='slays',default='V8,W8-0C0B120,W8-0C9B120,W8-12C0B120,SUR,SUR75',help='Names to display in the tables for each table. Ensure oder matches the --dlays names')
  opt.add_option('-d','--decs',dest='decs',default='-10,-30,-50',help='Declinations in stats file')
  opt.add_option('-f','--freqs',dest='freqs',default='650,800,1000,1400',help='Freqs in stats file')
  opt.add_option('-w','--weights',dest='weights',default='natural weighting',help='Weights in stats file')
  opt.add_option('-r','--resbins',dest='resbins',default=9,type='int',help='Number of resolution bins in stats file')
  opts,args = opt.parse_args(sys.argv[1:])
#-------------
  CPT["speed"] = "Relative (w.r.t SUR at 800MHz) survey speeds for the different layouts, calculated using the FOV \
(using PAF FOV for SKASUR) values given in the SRD \\cite{srd} and the values in table \\ref{tab:snr10-%s}. These values \
are generated at 650, 800 and 1000MHz for angular scales \\{0.4-1, 0.4-2, 1-2, 2-3, 3-4, 3-10, 10-60, 10-100, 600-3600\\} arcsec and are \
labelled {\\it resbin} \\{1, 2, 3, 4, 5, 6, 7, 8, 9\\} respectively at declination -30 degrees. \
%s."%(opts.label,CLR)

  CPT["speed_avg"] = "Relative (w.r.t SUR) average survey speeds for the different layouts, calculated using the FOV \
(PAF FOV for SKASUR) values given in the SRD \\cite{srd} and the values in table \\ref{tab:snr10-%s}. These values are \
generated for angular scales \\{0.4-1, 0.4-2, 1-2, 2-3, 3-4, 3-10, 10-60, 10-100, 600-3600\\} arcsec and are labelled {\\it resbin} \\{1, 2, \
3, 4, 5, 6, 7, 8, 9\\} respectively. This is done for natural weighting at declination -30 degrees. \
%s."%(opts.label,CLR)

#-------------
  std = open(args[0])
  hdr = std.readline()
  std.close()
  hdr = hdr[2:-1]
  names = hdr.split()
  dtype = ["float64"]*len(names)
  dtype[0],dtype[5],dtype[7] = ["S30"]*3
  decs = opts.decs.split(',')
  ndecs = len(decs)
  #weights = "natural weighting,robust-2 weighting ,robust-2 weighting with a 1 arcsec Gaussian taper".split(",")
  weights = opts.weights.split(',')
  nwi = len(weights)
  freqs = opts.freqs.split(',')
  nfreqs = len(freqs)
  decsWeights = {}
  for d in decs:
    for j,w in enumerate(weights):
       decsWeights["%s:%d"%(d,j)] = "DEC=%s, %s"%(d,w)
  lays = opts.lays.split(',')
  nlays = len(lays)
  Stats = np.genfromtxt(args[0],names=names,dtype=dtype)
  stats = Stats[np.argsort(Stats,order=["dec","widx","lo0","freq","ridx"])]
  #print stats
  resbins = opts.resbins
  STATS = {}
  metrics = names[9:]
  for n in range(nlays*ndecs*nwi):
    start,end = n*resbins*nfreqs,(n+1)*resbins*nfreqs
    res = stats[start:end]
    #print res
    s = {}
    for freq in range(nfreqs):
      tmp = "%d:%s:%d"%(res["dec"][0],res["lo0"][0],res["widx"][0])
      print tmp,"\n------------------"
      for metric in metrics:
       vals = res[metric]
       s[metric] = vals
      STATS[tmp] = s
  METRIC = {}
  for wi in range(nwi):
   wi = str(wi)
   for dec in decs:
    LAY = {}
    for item in STATS.keys():
      if item.endswith(wi):
        if item.startswith(dec):
            for metric in metrics:
                for lay in lays:
                    key = "%s:%s"%(dec,wi)
                    if item.split(":")[1]==lay:
                        LAY.setdefault(lay,[]).append([metric,STATS[item][metric]])
                METRIC[key] = LAY
  def get_table(met,lays):
   final = {}
   for item in METRIC.keys():
    data = []
    for lay in lays:
        #print METRIC[item].keys()
        for i in METRIC[item][lay]:
            if i[0]==met: 
                data.append(i[1].tolist())
    final[item] = [lays,np.array(data)]
   return final
  dec_flag = True
  exclude = ["flux10","relnoise","noise50_ref2","psf_xyBPA","psf_area"]
  # only include these layouts in the write up
  lays = opts.dlays.split(',')
  nlays = len(lays)
  for metric in metrics:
   if metric not in exclude:
    final = get_table(metric,lays)
    try: texname = "%s-%s.tex"%(metric,sys.argv[2])
    except IndexError: texname = "%s.tex"%(metric) 
    texfile = open(texname,"w")
    texfile.write("% Auto generated table\n \\begin{table}[!htp]\n \\renewcommand\\tabcolsep{2.8pt} \\tiny{\n")
    ncols = resbins*nfreqs + 1
    lays_print = opts.slays.split(',')
    nrows = len(lays_print)
    fmt =  repr(["$(c%d)s"%d for d in range(ncols)]).strip("[]").replace("'","").replace(","," &").replace("$","%")
    cols = ["c%d"%d for d in range(ncols)]
    keys = final.keys()
    keys.sort()
    if metric not in ["hours","snravg","speed_avg"]:
     for key in keys:
      x = final[key][1] 
      if metric.startswith('speed'):
         nm = x[-2,resbins:(2*resbins)].copy()
         for j in range(resbins*nfreqs):
           if (j>=resbins)&(j<2*resbins): jj = j - resbins
           elif (j> (resbins-1)*2 +1)&( j<3*resbins  ): jj = j - 2*resbins 
           elif (j> (resbins-1)*3 +1): jj = j - 3*resbins 
           else: jj = j
           x[:,j] = x[:,j]/nm[jj]
      typ = ["S30"]*ncols
      dtype = [item for item in zip(cols,typ)]
      s = np.ndarray([x.shape[0],x.shape[1]+1],dtype="S100")
      s[:,0] = lays_print
      s[:,1:(resbins+1)] = color(x[:,:resbins])
      s[:,(resbins+1):(2*resbins+1)] = color(x[:,resbins:(2*resbins)])
      s[:,(2*resbins+1):(3*resbins+1)] = color(x[:,(2*resbins):(3*resbins)])
      s[:,(3*resbins+1):(4*resbins+1)] = color(x[:,(3*resbins):(4*resbins)])
      rbins = 'c'*resbins
      fbins = 'l|%s'%rbins
      for i in range(1,nfreqs): fbins += '||%s'%rbins
      multicol = ''
      for freq in freqs:
        multicol += ' & \\multicolumn{%d}{c}{%sMHz}'%(resbins,freq)
      cols_str = ''
      for i in range(1,resbins+1): cols_str += '& %d '%i
      cols_str = cols_str*nfreqs
      if opts.oneDec: dec_flag = key.find(opts.oneDec)>=0
      if dec_flag:
       top = "\\subfloat%s{\\begin{tabular}{|%s|} \n \\tabularnewline \\cline{2-%d} \\multicolumn{1}{c}{ } %s \\tabularnewline \\cline{1-%d} \n resbin %s \\tabularnewline \\hline\n"%('' if opts.oneDec else '[%s]'%decsWeights[key],fbins,resbins*nfreqs+1,multicol,resbins*nfreqs+1,cols_str) 
       texfile.write(top)
       for row in range(nrows):
        for i,col in enumerate(cols): 
         locals()[col] = s[row,i]
        texfile.write(fmt%locals()+"%s \\hline \n"%('\\tabularnewline' if (nrows-row) == 1 else '\\\\'))
       #print "-------------------------------------------\n",fmt%locals()
       texfile.write("\\end{tabular}}\\hfill \n")
    else :
      print metric
      ncols = resbins + 1
      cols = ["c%d"%d for d in range(ncols)]
      typ = ["S30"]*ncols
      dtype = [item for item in zip(cols,typ)]
      s = np.ndarray([nlays,ncols],dtype="S100")
      fmt1 =  repr(["$(c%d)s"%d for d in range(ncols)]).strip("[]").replace("'","").replace(","," &").replace("$","%")
      s[:,0] = lays_print
      for i,key in enumerate(keys,start=0):
        if opts.oneDec: dec_flag = key.find(opts.oneDec)>=0
        s = np.ndarray([nlays,resbins+1],dtype="S100")
        s[:,0] = lays_print
        counter = range(0,ndecs*len(weights),ndecs)
        if i%nwi == 0:
          x = final[key][1]
          if metric.startswith('speed'):
           for j in range(resbins):
             x[:,j] = x[:,j]/x[-2,j]
          s[:,1:(resbins+1)] = color(x[:,:resbins])
          rbins = 'c'*resbins
          fbins = '|l|%s|'%rbins
          cols_str = ''
          for i in range(1,resbins+1): cols_str += '& %d '%i
          if dec_flag:
            top = "\\subfloat%s{\\begin{tabular}{%s} \\hline \n resbin %s\\tabularnewline \\hline\n"%('' if opts.oneDec else '[%s]'%decsWeights[key],fbins,cols_str)
            texfile.write(top)
            for row in range(nrows):
              for i,col in enumerate(cols): 
        #       print i,col,s[row,i]
               locals()[col] = s[row,i]
              texfile.write(fmt1%locals()+"%s \\hline \n"%('\\tabularnewline' if (nrows-row) == 1 else '\\\\'))
            #print "-------------------------------------------\n",fmt1%locals()
            texfile.write("\\end{tabular}}\\hfill \\\\\n")
    texfile.write("\n"+caption(metric)+"\\label{tab:%s-%s}"%(metric,sys.argv[2]))
    texfile.write("}\n \\end{table}")
    texfile.close()
