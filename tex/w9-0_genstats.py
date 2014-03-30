# auto-generated noise stats file
settings = dict(MKLO_NCHAN=1,MKLO_BW=50000.0,XWEIGHTS='uniform',MEASURE_NOISE=True,LOG_DISABLE=None,SCWEIGHT='uniform',NPIX_PSF=1024,MEASURE_PSF=False,LOG_FLUSH=None,SEFD=400,OUTDIR='W9-0A72',ARCSEC=4.84813681109536e-06,OUTFILE='W9-0A72/plots-SKA1REF2_8h60s_dec-10_650MHz_1ch/SKA1REF2_8h60s_dec-10_650MHz_1ch',FOVNORM=1000000000.0,SIDELOBES_R1_ARCSEC=1800,JOBS=2,LABEL='',WAVELENGTH=0.46153846153846156,SCWEIGHTFOV='512arcsec',BASEFREQ=650000000.0,LSM=None,BANDWIDTH=None,DOALL=True,SIMSCRIPT='turbo-sim.py',CELLSIZE_PSF='.05arcsec',FOV=120,SIDELOBES_CELL_ARCSEC=0.5,MKLO_BASE='SKA1REF2',ARCMIN=0.0002908882086657216,VERBOSE=1,PYXIS_LOAD_CONFIG=True,SUFFIX='spw0',MS='MSX/SKA1REF2_8h60s_dec-10_650MHz_1ch.MS',TAPER=0,SKIPNOISE=False,NO_X11=True,QUIET=None,MAKEMS_OUT='MSX',MAKEMS_REDO=False,RFI=False,RESBINS=((0.4, 1), (1, 2), (2, 3), (3, 4), (600, 3600)),XWEIGHTS0='natural',MSLIST='W9-0A72/mslist.txt',FILLIMAGE='SimsCont_Cosm/toycube/im0.fits',PYXIS_AUTO_IMPORT_MODULES=False,SKIPFILL=False,UVSTEP=0,XW=False,MKLO_NBAND=1,SCTAPER=1,JOB_STAGGER=10,XFOVS=(10, 120),LOG='W9-0A72/plots-SKA1REF2_8h60s_dec-10_650MHz_1ch/log-SKA1REF2_8h60s_dec-10_650MHz_1ch.txt',SIMJOB='simulate',STEP=1,WEIGHTS='natural:robust=-2,fov=10:robust=-2,fov=10,taper=1',STATSFILE='W9-0A72/genstats.py',PERSIST=None,FWHM=2.3548200450309493,MEASURE_SIDELOBES=False,CUBE_IMAGE='SKA1REF2_8h60s_dec-10_650MHz_1ch.1chan.fits',UVBINS=None,SCROBUST='',DEG=0.017453292519943295,XTAPERS=('', ',taper=1', ',taper=3'),UVFRACBINS=None,STATQUALS=('SKA1REF2_8h60s_dec-10_650MHz_1ch',),INTEGRATION=None,FILLIMAGE_SPWIDS=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],LOG_HEADER='## Tue Mar 25 16:04:26 2014:\n/home/makhathini/MeqTrees/Owlcat/pyxis OUTDIR=W9-0A72 -j2 noise_resuv_all',SIDELOBES_R0_ARCSEC=900,DESTDIR='W9-0A72/plots-SKA1REF2_8h60s_dec-10_650MHz_1ch')
noisestats = {}
noisestats.setdefault('freq0',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch'] = 650000000.0
noisestats.setdefault('wavelength',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch'] = 0.46153846153846156
noisestats.setdefault('bw',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('freq0',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch'] = 800000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch'] = 0.375
noisestats.setdefault('bw',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch'] = 8.9171613645177059e-07
noisestats.setdefault('pixnoise0',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch'] = 9.7845780866787519e-07
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.67138725691907319, 0.63487282784808352, 0.65313004238357841)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.74250276543515004, 0.64833203046609245, 0.6954173979506213)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',0.4,1.0,'natural','taper=0'] = 2.847352872840799e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',0.4,1.0,'natural','taper=0'] = 1.8816111916037206e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (0.7586957586519445, 0.70247228959641794, 0.73058402412418122)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (0.67091297179885323, 0.6053213349274843, 0.63811715336316877)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 3.2291032751811607e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 2.6964220480243997e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.0632016196922704, 1.0065584777353425, 1.0348800487138066)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (0.93970149412586435, 0.90815099013155232, 0.92392624212870833)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 3.0278293809147857e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 2.437464498717958e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.3468252006272767, 1.3138956590363648, 1.3303604298318208)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.2766482953631029, 1.2996796353647249, 1.2881639653639139)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.9776683981655075e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',1.0,2.0,'natural','taper=0'] = 3.0089232236196408e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (1.2322374853807492, 1.2155476644558705, 1.2238925749183098)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (1.1458862587526268, 1.1375902011464716, 1.1417382299495493)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 3.9221887020075058e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 3.3212892981021706e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.3366994258258293, 1.315143630397577, 1.3259215281117032)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (1.2470422247923161, 1.2416239807490999, 1.2443331027707081)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 3.7038375626563731e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 3.3094011391153363e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.3827844136788094, 2.2870374865398295, 2.3349109501093195)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.4371293194740886, 2.2610873076928799, 2.3491083135834843)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',2.0,3.0,'natural','taper=0'] = 3.9277895540181315e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',2.0,3.0,'natural','taper=0'] = 4.2315852330622158e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (2.2534790794779922, 2.2457149398923324, 2.2495970096851625)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (2.245088036406754, 2.2214151962338633, 2.2332516163203087)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 5.0978670061037411e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 5.0671223494313335e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (2.2752210995294675, 2.2668524065520583, 2.2710367530407627)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (2.2665411462262566, 2.2443117568797017, 2.2554264515529789)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 5.0309621366846183e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 4.993859505042132e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4187841055019348, 3.188051081002957, 3.3034175932524459)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',3.0,4.0,'natural','taper=0'] = 5.2405288732095205e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (3.2554897472112194, 3.253675678530644, 3.2545827128709317)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4810507969599822, 3.2264728822131401, 3.3537618395865612)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',3.0,4.0,'natural','taper=0'] = 4.6959563514304928e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 5.936216776801941e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (3.2507018677412471, 3.27293597134712, 3.2618189195441838)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (3.2639658095844202, 3.2618220549859847, 3.2628939322852024)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 5.5794682775649851e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 5.9204670515460918e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (3.2589830574160552, 3.280695139249302, 3.2698390983326786)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 5.5554152710171874e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = (808.21150166123016, 782.88327120330621, 795.54738643226824)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = (803.84351685915465, 802.32441302851214, 803.08396494383339)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.3507444401689454e-05
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = 9.651261645153268e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (807.86831150246405, 782.60437890803576, 795.2363452052499)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (749.61589133419886, 740.84135647732808, 745.22862390576347)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 1.3507744918031259e-05
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 9.4473659433543742e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (807.86841180055535, 782.60444833400038, 795.23643006727787)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (749.61604813332849, 740.8415322591045, 745.22879019621655)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 1.3507744404333815e-05
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 9.4473633726767794e-06
noisestats.setdefault('freq0',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch'] = 1100000000.0
noisestats.setdefault('wavelength',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch'] = 0.27272727272727271
noisestats.setdefault('bw',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('freq0',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch'] = 650000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch'] = 0.46153846153846156
noisestats.setdefault('bw',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch'] = 9.3831370464751585e-07
noisestats.setdefault('pixnoise0',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch'] = 1.0020771778047836e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.60608887918325949, 0.56838294382072851, 0.58723591150199406)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.80644447156112531, 0.76231577478506052, 0.78438012317309291)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = 2.5447202803408675e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',0.4,1.0,'natural','taper=0'] = 2.2452067459015543e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (0.53346839756301634, 0.49612531982073177, 0.51479685869187408)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (0.81420317282432908, 0.76114727738319521, 0.7876752251037622)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 3.09771104639346e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 2.9181001096929262e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (0.94148021982985508, 0.90880334845385513, 0.92514178414185511)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.0407960856647043, 0.99755336948929496, 1.0191747275769996)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 2.8746981707035126e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 2.4923123923906367e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.3879259441337319, 1.2775015322217629, 1.3327137381777474)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.9711835085388158e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.2316917092937689, 1.1926307949650061, 1.2121612521293876)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (1.1883703510828783, 1.1647526915815274, 1.1765615213322027)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.2981623899675976e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 3.8946164079828884e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (1.1724953412479209, 1.1481563109287274, 1.1603258260883242)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (1.2875003182259916, 1.2666491659769283, 1.2770747421014601)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 2.9011276719725952e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 3.5322448959483361e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.2638562024149302, 1.2457391737389965, 1.2547976880769633)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 2.9477103946725005e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.4196633034526562, 2.2842270919356369, 2.3519451976941466)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = 4.0158147770435217e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.4306927432008512, 2.2626595892769403, 2.346676166238896)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',2.0,3.0,'natural','taper=0'] = 4.2147819852850241e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (2.2416155519730183, 2.2361574833903455, 2.2388865176816819)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (2.2430615270217249, 2.2518984039786907, 2.247479965500208)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 4.2286793545466015e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 5.530042564850301e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (2.2644738423833002, 2.2594175956352247, 2.2619457190092627)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (2.2655978822206291, 2.2725386028577894, 2.269068242539209)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 4.151646760496626e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 5.4699460039130872e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4398076550089054, 3.2560991398754076, 3.3479533974421565)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = 4.7742485711971529e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4226014618383145, 3.2711227121181512, 3.3468620869782328)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',3.0,4.0,'natural','taper=0'] = 4.970325049923156e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (3.2615611702884677, 3.236303598306868, 3.2489323842976678)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (3.2634466219972755, 3.2440459961923676, 3.2537463090948213)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 4.4959977099727757e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 6.3399567938438444e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (3.2699802885459937, 3.2453013384951657, 3.2576408135205797)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (3.2713643320697754, 3.2521097556341765, 3.2617370438519759)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 4.4715852938455333e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 6.3175316607300468e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = (784.80611104637705, 733.59292907429597, 759.19952006033645)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.859460731218252e-05
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (782.53389708428892, 731.66534201577406, 757.09961955003155)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = (814.84890619167641, 789.50275710260019, 802.17583164713824)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.0141876888834287e-05
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 1.8665784047286109e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (752.17340424480824, 726.13991387929923, 739.15665906205368)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (782.53399830202477, 731.66542768511238, 757.09971299356857)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 9.8025986738164251e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 1.8665784790774167e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (752.17357330949073, 726.14011864937277, 739.15684597943175)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 9.8025979659537067e-06
noisestats.setdefault('freq0',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch'] = 1100000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch'] = 0.27272727272727271
noisestats.setdefault('bw',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch'] = 9.4626343764276913e-07
noisestats.setdefault('freq0',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch'] = 800000000.0
noisestats.setdefault('wavelength',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch'] = 0.375
noisestats.setdefault('bw',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch'] = 9.2417011348872825e-07
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.5854679114798268, 0.51960591537118661, 0.5525369134255067)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = 1.778838978009863e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.61696395979137086, 0.58133122033324092, 0.59914759006230589)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (0.5454606466687455, 0.50868108344134766, 0.52707086505504663)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',0.4,1.0,'natural','taper=0'] = 2.5568516970973614e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 2.6021892715686361e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (0.63926733968242644, 0.59170398825880444, 0.61548566397061544)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (0.87612511013440741, 0.86706976794506352, 0.87159743903973541)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 3.1800058065197218e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 2.7374556938323295e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (1.0056024659520115, 0.96199450012497578, 0.9837984830384936)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 3.0888754786909586e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.3829518587451903, 1.2954898399695851, 1.3392208493573876)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = 3.2366233216260817e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (1.1681674019305126, 1.1685090139421381, 1.1683382079363254)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.3703688399741589, 1.2891618385210191, 1.329765339247589)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 4.0649675298729779e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.9352722757111295e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (1.2689073081218254, 1.2662711015307384, 1.2675892048262818)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (1.2181507131017679, 1.1945559892596556, 1.2063533511807116)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 3.7788027563834221e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 4.0575340089291632e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (1.3195902392257939, 1.2939277362802362, 1.306758987753015)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 3.7978064793878714e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.3731367392910814, 2.2954924411733821, 2.334314590232232)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = 4.6043073534650389e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (2.2375629492643143, 2.2313175926285984, 2.2344402709464566)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 4.9135929436688106e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.3777905633616965, 2.3229521783978346, 2.3503713708797656)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (2.2595109974223968, 2.2539477815869637, 2.2567293895046801)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',2.0,3.0,'natural','taper=0'] = 4.0097481017790719e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 4.8688908232399623e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (2.2570069373707229, 2.2310812728159979, 2.2440441050933604)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 5.0292045081069852e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (2.2777451081736291, 2.2539940868057911, 2.2658695974897101)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 4.9591206963743888e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.3898908819718989, 3.3468956378786729, 3.3683932599252859)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = 6.190370778144689e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4419327805875759, 3.2417153497527775, 3.3418240651701767)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (3.2517026838758976, 3.2534778785197815, 3.2525902811978398)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',3.0,4.0,'natural','taper=0'] = 4.8259802256369575e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 6.2874527156846356e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (3.2542139899073628, 3.2517617196327047, 3.2529878547700335)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (3.2606219224943009, 3.262213038609064, 3.2614174805516827)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 5.3003622286170676e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 6.2518379625324249e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (3.2624997964239371, 3.259983980897283, 3.26124188866061)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 5.2773761641022047e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = (805.4010695188116, 779.2312186252085, 792.31614407201005)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.1985445203804693e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = (777.35080250852707, 749.37215280630869, 763.36147765741794)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (804.62231654359778, 779.07190968052487, 791.84711311206138)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.9075781754629052e-05
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 1.1985710356930077e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (777.64474689648262, 747.27747508674599, 762.46111099161431)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (804.62241840615877, 779.07202667477964, 791.84722254046915)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 1.9128173334905349e-05
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 1.1985712093721604e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (777.64485641987415, 747.27758312687308, 762.46121977337361)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 1.9128174785936461e-05
noisestats.setdefault('freq0',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch'] = 800000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch'] = 0.375
noisestats.setdefault('bw',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('freq0',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch'] = 650000000.0
noisestats.setdefault('wavelength',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch'] = 0.46153846153846156
noisestats.setdefault('bw',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch'] = 9.4159026753773269e-07
noisestats.setdefault('pixnoise0',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch'] = 9.5656497083961682e-07
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.72566612092396787, 0.68433562006671034, 0.7050008704953391)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.68770597773714071, 0.61340205978267848, 0.65055401875990959)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',0.4,1.0,'natural','taper=0'] = 1.9306595512941889e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',0.4,1.0,'natural','taper=0'] = 2.8067999755713068e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (0.67754214630046927, 0.63184176727822083, 0.654691956789345)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (0.74480779429117494, 0.68329580400996415, 0.71405179915056949)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 2.8692505346495016e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 2.9841577973955249e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (0.95028532429831347, 0.9207625093384304, 0.93552391681837199)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.0468878401919022, 1.0029584214907687, 1.0249231308413354)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 2.5708581490043456e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 2.8002952597511348e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.3105434600551182, 1.2390247363517835, 1.2747840982034508)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.3661289433785955, 1.3081050377321797, 1.3371169905553875)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.8150011693446239e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.9685852647362179e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (1.1486046468017046, 1.1476617448789308, 1.1481331958403178)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (1.2225083444123048, 1.1881818078904489, 1.2053450761513769)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 3.3579763702408338e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 3.6264629564316647e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (1.2468334681539255, 1.2478044093379417, 1.2473189387459336)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.32422492188019, 1.2932530636659143, 1.3087389927730522)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 3.3892326916509463e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 3.3869164925499148e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.3438003385732165, 2.3690718614567468, 2.3564361000149816)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',2.0,3.0,'natural','taper=0'] = 4.3175216574876672e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.4173922103742895, 2.2640763249340137, 2.3407342676541516)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (2.2580207261354177, 2.2278007252824916, 2.2429107257089544)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',2.0,3.0,'natural','taper=0'] = 3.8947032630850284e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 5.6012920352794388e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (2.2443423658950987, 2.2314996025428711, 2.2379209842189849)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (2.2784232036990733, 2.2504145331109107, 2.264418868404992)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 4.4407214365960748e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 5.5269860580878176e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (2.266464189614926, 2.254507372837137, 2.2604857812260315)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 4.3717069321243183e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4128408313611898, 3.2163392634351866, 3.3145900473981884)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',3.0,4.0,'natural','taper=0'] = 5.1681121281591343e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (3.2521757668211095, 3.2485120296258128, 3.2503438982234609)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 6.4884879504601527e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (3.2600150276919861, 3.2566734789300673, 3.2583442533110265)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 6.4787652874972681e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.3814699682571558, 3.3169423913244382, 3.349206179790797)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',3.0,4.0,'natural','taper=0'] = 4.7899751656986263e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (3.264663346024391, 3.2499599200892728, 3.2573116330568319)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 4.7910770829829464e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (3.2730736012379542, 3.258425210890092, 3.2657494060640229)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 4.7704322336691353e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = (809.7232308991064, 783.56859377501826, 796.64591233706233)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.2605178528548812e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (809.41889986981573, 782.97754743943983, 796.19822365462778)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 1.2602124648154297e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (809.41906688861638, 782.9776762792518, 796.19837158393409)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 1.2602125749380288e-05
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = (807.17882220673221, 792.48894287479925, 799.83388254076567)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.0160685070343286e-05
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (751.66523410537138, 734.94735739084649, 743.30629574810894)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 9.8410624415359789e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (751.66545302418251, 734.94753518285438, 743.30649410351839)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 9.8410617364399394e-06
noisestats.setdefault('freq0',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch'] = 1100000000.0
noisestats.setdefault('wavelength',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch'] = 0.27272727272727271
noisestats.setdefault('bw',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch'] = 1.0074066180427643e-06
noisestats.setdefault('freq0',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch'] = 650000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch'] = 0.46153846153846156
noisestats.setdefault('bw',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch'] = 9.4880292780568022e-07
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.60469573950917255, 0.5666081457922888, 0.58565194265073073)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = 2.5493490412309802e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (0.54270184841237967, 0.51260232833612007, 0.52765208837424993)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 3.2399001733230844e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (0.94948982969474272, 0.92425738599712015, 0.93687360784593143)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 3.1056791427435883e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.84870636717233627, 0.73098030590672569, 0.78984333653953098)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',0.4,1.0,'natural','taper=0'] = 2.1310588803124867e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (0.80813720878233108, 0.74612425191829057, 0.77713073035031077)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 2.7202307882025202e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.0252277964109013, 0.99071958181754771, 1.0079736891142246)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 2.2817227266507709e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.3371055509978751, 1.3159780084815647, 1.3265417797397199)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = 3.0364651038579514e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (1.1919423712680948, 1.187375158595906, 1.1896587649320005)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.200248074488486, 1.2179185902258265, 1.2090833323571561)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.3586087584614275e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 4.2523095468907056e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (1.1545730985928144, 1.1370840863573191, 1.1458285924750666)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (1.2901832383401295, 1.2850913965959283, 1.2876373174680289)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 2.6356516070124742e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 3.8812624431724583e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.25067965234462, 1.2388127901328252, 1.2447462212387226)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 2.7288191665367033e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.4297249868359225, 2.265805809841535, 2.347765398338729)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = 4.0121134387129569e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (2.2435633606517964, 2.2339944160420222, 2.2387788883469093)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.3846448952975834, 2.2978396601164328, 2.3412422777070079)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 4.5907902372948786e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',2.0,3.0,'natural','taper=0'] = 4.3372227252070292e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (2.2659851456652871, 2.2567844305028091, 2.2613847880840483)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (2.2440345417318266, 2.2496842985668741, 2.2468594201493506)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 4.5195110743938092e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 4.9117919033580291e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (2.2664909407886538, 2.2713436685054482, 2.2689173046470508)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 4.8438700403121647e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4006848608463027, 3.3043510957962181, 3.3525179783212602)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = 4.6977472689375713e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (3.2542631827992672, 3.2570587532007442, 3.2556609680000057)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 4.7748106406445828e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (3.2627732880577431, 3.2654302958153187, 3.2641017919365307)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4302973625860953, 3.2714240106381913, 3.3508606866121431)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 4.7480954900510742e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',3.0,4.0,'natural','taper=0'] = 5.0628058884546469e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (3.2641333408124886, 3.2387553275396423, 3.2514443341760657)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 5.4692507949449596e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (3.2724396830727516, 3.2472396960966248, 3.2598396895846884)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 5.44298314251749e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = (784.8455926208012, 742.37225618415221, 763.60892440247676)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.7241906415371508e-05
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (782.3587624222821, 740.63831464598934, 761.49853853413572)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 1.7280211904981379e-05
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (782.35877824686872, 740.63835027613482, 761.49856426150177)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 1.7280212708084233e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = (809.86538698935499, 789.39516699050182, 799.63027698992846)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.0587577818430592e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (747.57332575509929, 738.89349350409088, 743.23340962959514)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 1.032873769143261e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (747.57363117606269, 738.89373804579441, 743.23368461092855)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 1.0328738363237227e-05
noisestats.setdefault('freq0',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch'] = 1100000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch'] = 0.27272727272727271
noisestats.setdefault('bw',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch'] = 9.5951951782182636e-07
noisestats.setdefault('freq0',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch'] = 800000000.0
noisestats.setdefault('wavelength',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch'] = 0.375
noisestats.setdefault('bw',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch'] = 9.2488194927956416e-07
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.57959055251883818, 0.5493034647026559, 0.56444700861074704)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = 1.7677359306365217e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (0.55616459553366859, 0.52915835054217975, 0.54266147303792422)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 2.7587648560860735e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.62897628413707063, 0.56560859381982764, 0.59729243897844908)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (0.87914157732110698, 0.86890999413753711, 0.8740257857293221)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',0.4,1.0,'natural','taper=0'] = 2.5358584921250241e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 2.8837141405133922e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (0.62027557986406445, 0.57148899537568221, 0.59588228761987327)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 2.9441425223277524e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (0.98750997088835213, 0.95629438688867296, 0.97190217888851249)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 2.8431730023925551e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.3155821095116504, 1.328421873803973, 1.3220019916578116)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = 3.1933273400301261e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (1.1606725440354002, 1.1878799634661437, 1.1742762537507718)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 4.3210742016179909e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (1.2602465826811724, 1.2819705821027207, 1.2711085823919466)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.3723875423341203, 1.282166286552576, 1.3272769144433481)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 4.0685131266823084e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.9713493171196454e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (1.1941180387932397, 1.1799177621986972, 1.1870179004959684)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 3.7800457052788182e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (1.2950897203150136, 1.2802552131581135, 1.2876724667365635)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 3.4735592887995612e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.4347701647508058, 2.2383400511711415, 2.3365551079609737)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = 4.4689342704142979e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (2.2382431523781663, 2.2399543120903602, 2.2390987322342633)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.4453486806616307, 2.2703062576357174, 2.357827469148674)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 5.5578057170759474e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',2.0,3.0,'natural','taper=0'] = 3.9560359834956063e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (2.2603431276753243, 2.2616137737379747, 2.2609784507066495)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (2.2427754816289589, 2.2316973183395374, 2.2372363999842482)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 5.5074542977351847e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 4.342105110787099e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (2.26530416005706, 2.2548610175794983, 2.2600825888182792)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 4.2699493696068561e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.2999190253189665, 3.4433492445178144, 3.3716341349183905)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = 6.0804823432769091e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (3.2659262367108401, 3.2415332230894531, 3.2537297299001464)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4890338686177347, 3.199072326268328, 3.3440530974430311)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 6.8131847406587396e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',3.0,4.0,'natural','taper=0'] = 4.7747770346027342e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (3.2741341531107184, 3.2502348503338574, 3.2621845017222881)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (3.2559798088306335, 3.2372977293852192, 3.2466387691079266)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 6.7765109205030402e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 4.6407180577487255e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (3.2642786425606225, 3.2461114834001559, 3.2551950629803894)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 4.6192003656846204e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = (770.9986759939228, 775.61000754096528, 773.30434176744404)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.7930930935639377e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (771.55658159726568, 771.809846173192, 771.68321388522884)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 1.7934466801208701e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (771.55669708710036, 771.80993225134375, 771.683314669222)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 1.7934469122624842e-05
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = (801.41269109695679, 777.73366152079745, 789.57317630887712)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.2926372454840332e-05
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (800.56000249742999, 777.16545397886739, 788.86272823814875)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 1.2934055556139357e-05
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (800.56016087045066, 777.16560042619699, 788.86288064832388)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 1.2934055556139357e-05
noisestats.setdefault('freq0',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch'] = 650000000.0
noisestats.setdefault('wavelength',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch'] = 0.46153846153846156
noisestats.setdefault('bw',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch'] = 9.467650096365333e-07
noisestats.setdefault('freq0',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch'] = 800000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch'] = 0.375
noisestats.setdefault('bw',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch'] = 8.9863990380304787e-07
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.69110273796668564, 0.60222764248922944, 0.64666519022795754)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',0.4,1.0,'natural','taper=0'] = 2.7540584851282964e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (0.75621619530843409, 0.6668192447020922, 0.71151772000526314)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 3.0311631233051593e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.0574142181407968, 0.98826915032276852, 1.0228416842317827)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 2.8545067297676618e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.7392517797110375, 0.66269087546579586, 0.70097132758841663)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',0.4,1.0,'natural','taper=0'] = 1.9139733698402157e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (0.66662439247887795, 0.61750471603402246, 0.64206455425645026)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 2.6729129066058321e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (0.93676229541932254, 0.91625349894478347, 0.92650789718205306)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 2.4133873679294747e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.3868374697546355, 1.2893525666218904, 1.3380950181882629)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.9808574689826061e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (1.2344655424539068, 1.1796570609797998, 1.2070613017168532)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 3.7204234035608149e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.3371654410911353, 1.2828004853200192, 1.3099829632055773)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 3.4997822319706006e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.2727193170763367, 1.2848533199543444, 1.2787863185153405)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.9608120066316327e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (1.1425842907487567, 1.1420206353042706, 1.1423024630265135)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 3.2223098920691788e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (1.2442883100391127, 1.2457086327158033, 1.244998471377458)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 3.1991765499495055e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.4399014613688976, 2.2530651277916873, 2.3464832945802927)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',2.0,3.0,'natural','taper=0'] = 3.856760499496197e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (2.2586831722276246, 2.2216980208235029, 2.2401905965255637)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 4.7270275240756529e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (2.2799852306366648, 2.2451047960607422, 2.2625450133487037)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 4.6533414778675299e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.3905228618884737, 2.3097159557418805, 2.3501194088151771)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',2.0,3.0,'natural','taper=0'] = 4.3047526721084949e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (2.2332915267396833, 2.2278593518204342, 2.2305754392800585)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 4.7337298782869073e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (2.256004821621191, 2.2506455057082895, 2.2533251636647402)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 4.6639713991168286e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4728536417616818, 3.2660194923986161, 3.3694365670801489)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',3.0,4.0,'natural','taper=0'] = 4.7725508795760375e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (3.2688593597793889, 3.2421344577856428, 3.2554969087825159)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4716079634105057, 3.1655083747920281, 3.3185581691012667)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',3.0,4.0,'natural','taper=0'] = 5.1514449561829188e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 4.9525725776689644e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (3.2401594083806562, 3.2552196630979355, 3.2476895357392959)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (3.2770807489845688, 3.2506081935581301, 3.2638444712713497)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 5.5147459216435129e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 4.9340105872685858e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (3.2486899921919994, 3.2633922763959298, 3.2560411342939646)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 5.5023830320910928e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = (804.35250467937794, 790.22329223252677, 797.28789845595236)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.0186675366369316e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = (814.83373085062988, 767.19235099598893, 791.0130409233094)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (757.93031025420726, 717.11410284532758, 737.52220654976736)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.323700540461406e-05
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 9.9755017839991463e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (814.6162963392901, 767.08214032391413, 790.84921833160206)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (757.93053276658043, 717.11437254360908, 737.52245265509475)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 1.323424046286312e-05
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 9.9755017839991463e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (814.61642044829398, 767.08228372327676, 790.84935208578531)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 1.3234241511490527e-05
noisestats.setdefault('freq0',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch'] = 650000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch'] = 0.46153846153846156
noisestats.setdefault('bw',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch'] = 9.4728660314164352e-07
noisestats.setdefault('freq0',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch'] = 1100000000.0
noisestats.setdefault('wavelength',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch'] = 0.27272727272727271
noisestats.setdefault('bw',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch'] = 9.2648155088334158e-07
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.85484188397186678, 0.71791480179649769, 0.78637834288418218)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',0.4,1.0,'natural','taper=0'] = 2.1179848994092866e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.60049113373389562, 0.56539236518175207, 0.58294174945782384)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (0.81127254167156337, 0.72708183000739379, 0.76917718583947858)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = 2.5226964614614786e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 2.7546624728147893e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (0.52229999146780759, 0.50357947697067995, 0.51293973421924377)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 3.0455949870941632e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.0280629267821291, 0.977299145341191, 1.00268103606166)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 2.3554007776998653e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (0.93145424533653132, 0.91282512949777639, 0.92213968741715391)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 2.794944355316004e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.2137628437502788, 1.2079331508946083, 1.2108479973224435)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.3891809601321751e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.3661409110141352, 1.3022492669803787, 1.3341950889972569)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (1.155389882001526, 1.1383032935624524, 1.1468465877819893)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = 3.0012385477418263e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 2.7257449145467628e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (1.1778196574376911, 1.168960488874436, 1.1733900731560636)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.2512468539944834, 1.2387418604000522, 1.2449943571972679)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 3.7953969392382887e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 2.8088446446100537e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (1.2782910017543259, 1.2711224233642338, 1.2747067125592797)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 3.4170218916752966e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.4001371699880094, 2.3017817325730352, 2.3509594512805223)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',2.0,3.0,'natural','taper=0'] = 4.3331195758952872e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.4144749492141937, 2.2662671079722441, 2.3403710285932187)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (2.2572270280591882, 2.2403158629221083, 2.2487714454906484)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = 4.022467482045697e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 5.1041954263380266e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (2.239887763037848, 2.2337940959836677, 2.2368409295107581)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (2.2789101366184386, 2.2623908133062303, 2.2706504749623342)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 4.0574322551636282e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 5.0400183374891818e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (2.2630256650109901, 2.2573585812168391, 2.2601921231139146)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 3.9872735477447925e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4702444192313351, 3.2075610279918383, 3.3389027236115867)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',3.0,4.0,'natural','taper=0'] = 5.0597806662591245e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (3.2541086048051007, 3.2437078389392271, 3.2489082218721639)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 5.7495040554074167e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (3.2622506665999134, 3.2520536379010951, 3.2571521522505043)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 5.7266797166567413e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4064225306167017, 3.3130816676771695, 3.3597520991469354)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = 4.7877298086961735e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (3.2587556563430375, 3.2437876817947466, 3.2512716690688919)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 4.4281004782137118e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (3.2673949820283581, 3.2525816249922017, 3.2599883035102799)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 4.4021164125773592e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = (812.06103407036198, 784.12605720039983, 798.09354563538091)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.0715169250656323e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (754.77650229038056, 720.94225895269153, 737.85938062153605)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 1.0504177874699172e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (754.77675032097545, 720.94250477740843, 737.85962754919194)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 1.0504176553530694e-05
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = (793.7841661141681, 734.03884203817552, 763.91150407617181)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.8131569208405009e-05
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (792.02630678062712, 732.06307283070646, 762.04468980566685)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 1.8163240325539436e-05
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (792.0264261766448, 732.06319899069808, 762.0448125836715)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 1.8163242617716386e-05
noisestats.setdefault('freq0',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch'] = 800000000.0
noisestats.setdefault('wavelength',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch'] = 0.375
noisestats.setdefault('bw',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch'] = 9.0927291378695684e-07
noisestats.setdefault('freq0',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch'] = 1100000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch'] = 0.27272727272727271
noisestats.setdefault('bw',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch'] = 9.0567214847407136e-07
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.62644535176682692, 0.56988482612361635, 0.59816508894522169)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',0.4,1.0,'natural','taper=0'] = 2.6163598693232537e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (0.6314199543668978, 0.5598652213014218, 0.5956425878341598)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 2.9752832432867075e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.58420270019021059, 0.53012870207842555, 0.55716570113431807)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = 1.7745795080860258e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (0.99774048772735824, 0.94690599477820525, 0.9723232412527818)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (0.54044216465209693, 0.51544724953286869, 0.52794470709248276)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 2.8368580937757748e-06
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 2.5652401640712685e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (0.87462335522297308, 0.870119839168364, 0.87237159719566848)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 2.6916849754769433e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.3835783414046463, 1.275872085193146, 1.3297252132988961)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.951189751890977e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (1.2134391889351255, 1.1717471263291543, 1.1925931576321398)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 3.8637490413777473e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (1.3126610468816511, 1.2739801438414751, 1.2933205953615632)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.3658459155232607, 1.3106433291386854, 1.338244622330973)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = 3.2168954860403374e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 3.5645367513650639e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (1.1652638113403195, 1.1647526455699062, 1.1650082284551129)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 4.001468599513611e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (1.2652800028976621, 1.2652905788500894, 1.2652852908738756)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 3.6599423760243262e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.4176704021763427, 2.2845854745589085, 2.3511279383676253)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',2.0,3.0,'natural','taper=0'] = 4.0555801472160915e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (2.2457928639249918, 2.2396396302161592, 2.2427162470705753)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 4.4694396442076291e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.3818178485373345, 2.2820097352086317, 2.3319137918729833)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (2.2681524928439747, 2.2620589817935661, 2.2651057373187706)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = 4.4996130949013891e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 4.3955029614935641e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (2.2326417670666947, 2.2405117723819203, 2.2365767697243077)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 4.6501774575792814e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (2.2554134506677364, 2.2627646362448361, 2.259089043456286)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 4.6051559294372978e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4812112376990787, 3.2025457891672549, 3.3418785134331666)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',3.0,4.0,'natural','taper=0'] = 4.7933686431374874e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (3.2600144149038357, 3.2295496072626517, 3.2447820110832435)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 4.847673652516048e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.3460929918596665, 3.4347160186922765, 3.3904045052759715)
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (3.2680959164511383, 3.2384424441648192, 3.2532691803079787)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = 6.2575704477705646e-06
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 4.8236619019467709e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (3.2631227509365082, 3.2369663388216976, 3.2500445448791027)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 5.8971898449993388e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (3.2718405526345866, 3.2459958975929522, 3.2589182251137694)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 5.8667556587268425e-06
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = (801.01991795821789, 780.14857777149371, 790.5842478648558)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.2918931857379e-05
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (800.21331003735156, 779.31346899109133, 789.76338951422144)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 1.2926989224852246e-05
noisestats.setdefault('psf_fwhm',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (800.21341988621759, 779.31360005214731, 789.76350996918245)
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = (781.35578754068445, 755.1580155773695, 768.25690155902703)
noisestats.setdefault('pixnoise',{})['SKA1REF2_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 1.2926988688076519e-05
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.9050460758710688e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (781.66770552718845, 754.35125911866794, 768.00948232292819)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 1.9069827625727923e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (781.66775865575812, 754.35134738443378, 768.00955302009595)
noisestats.setdefault('pixnoise',{})['SKA1W9-0A72B120_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 1.9069828353463266e-05
noisestats.setdefault('freq0',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch'] = 800000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch'] = 0.375
noisestats.setdefault('bw',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch'] = 9.0675938262040217e-07
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.74124552532142296, 0.64746223740225151, 0.69435388136183729)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',0.4,1.0,'natural','taper=0'] = 1.7546240888464589e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (0.65709636335509669, 0.59341866714623903, 0.62525751525066786)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 2.5658380614979689e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (0.93757281875138943, 0.90728708358564647, 0.92242995116851789)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 2.1447135562463939e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.2898725208481845, 1.28980400506267, 1.2898382629554273)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.6538261054742292e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (1.1485158313412038, 1.1339140683606022, 1.141214949850903)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 2.8569499095940812e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (1.2490818822193137, 1.2376138456879084, 1.2433478639536111)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 2.8185694171070577e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.424114764805176, 2.2497733399396487, 2.3369440523724121)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',2.0,3.0,'natural','taper=0'] = 3.7852654833187032e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (2.2388602168425735, 2.2234090839925069, 2.2311346504175402)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 4.1209909481602423e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (2.2608237947607082, 2.2464039160385791, 2.2536138553996437)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 4.0651685239896249e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4121146178292676, 3.2102153082792202, 3.3111649630542441)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',3.0,4.0,'natural','taper=0'] = 4.8235817042548845e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (3.2550409205374322, 3.2259371476887608, 3.2404890341130965)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 4.8647103140941834e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (3.2631566365803955, 3.2347095429058212, 3.2489330897431081)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 4.8498313450949518e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = (801.2180553648285, 779.22112739511567, 790.21959137997214)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.3455954313784294e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (800.98495912072394, 778.84810607743987, 789.91653259908185)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 1.3453386009156478e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (800.98503315499215, 778.84817470476355, 789.91660392987785)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 1.3453386009156478e-05
noisestats.setdefault('freq0',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch'] = 1100000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch'] = 0.27272727272727271
noisestats.setdefault('bw',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch'] = 9.1477796912552672e-07
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.58209038088699727, 0.55227364552420399, 0.56718201320560069)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = 1.6583890479682354e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (0.54676195593910359, 0.52226419652188794, 0.53451307623049571)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 2.5622011915033972e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (0.8799948201438641, 0.86982050373632813, 0.87490766194009617)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 2.4591156825946538e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.3195181458150433, 1.3183145960626184, 1.318916370938831)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.7781158829875298e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (1.1609426325717596, 1.1729359258413139, 1.1669392792065367)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 3.6691666409587287e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (1.2598917446012508, 1.269019660259437, 1.264455702430344)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 3.4115995959308053e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.3921386352522904, 2.2499655545362436, 2.321052094894267)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = 3.9664915836811523e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (2.2279004639741617, 2.2347998887346483, 2.2313501763544048)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 4.366945433949117e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (2.2509953401944585, 2.2570184994503508, 2.2540069198224044)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 4.3202710131728046e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.3190564880957134, 3.3457098009059565, 3.3323831445008349)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = 5.2652843753547628e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (3.2497760119110062, 3.2461795497831507, 3.2479777808470782)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 5.4131458057172564e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (3.2579981616292608, 3.2548439345309741, 3.2564210480801172)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 5.3859346724610163e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = (759.34525016207442, 767.19584482079563, 763.27054749143508)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.8323892999270593e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (759.11496081116195, 764.46670934931342, 761.79083508023768)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 1.8307613125447033e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (759.11505195411951, 764.46679286512392, 761.79092240962177)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 1.8307615399548008e-05
noisestats.setdefault('freq0',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch'] = 650000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch'] = 0.46153846153846156
noisestats.setdefault('bw',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch'] = 8.5988126798112518e-07
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.80208984397722327, 0.75876535618464558, 0.78042760008093448)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',0.4,1.0,'natural','taper=0'] = 2.1162331606473231e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (0.7986789008618761, 0.74712654901060782, 0.7729027249362419)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 2.7645267046465922e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.0340246968882245, 0.99354408472145384, 1.0137843908048392)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 2.2511082891527288e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.2438682968818369, 1.203964101178723, 1.2239161990302798)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.1012610471657406e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (1.1720873549996498, 1.150420871680945, 1.1612541133402974)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 2.595430931857004e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.2654000406822254, 1.2485739292367601, 1.2569869849594928)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 2.5981198355161753e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.4052038320076137, 2.2911566928970997, 2.3481802624523569)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',2.0,3.0,'natural','taper=0'] = 3.6902603757599965e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (2.2407178282619271, 2.2376865709994243, 2.2392021996306757)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 4.5661694450611571e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (2.2630107609420635, 2.25937524656569, 2.2611930037538768)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 4.5097420250233625e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4456487716377864, 3.2444643460541416, 3.3450565588459638)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',3.0,4.0,'natural','taper=0'] = 4.4497974717877855e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (3.2569123724323306, 3.2502999395402705, 3.2536061559863008)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 5.2114334790640863e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (3.2649946786693693, 3.2584379540546267, 3.2617163163619978)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 5.1907647812071889e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = (800.21065427521421, 797.24677128138194, 798.72871277829813)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.0096659732042479e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (738.1380827059553, 733.86058347323217, 735.99933308959373)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 9.77981582840198e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (738.13832460165349, 733.86086766927167, 735.99959613546253)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 9.7798147641343502e-06
noisestats.setdefault('freq0',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch'] = 800000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch'] = 0.375
noisestats.setdefault('bw',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch'] = 8.866639379241686e-07
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.73727873407928246, 0.66136277379608666, 0.69932075393768456)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',0.4,1.0,'natural','taper=0'] = 1.7489948460303086e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (0.65232293605602842, 0.60490617361695886, 0.62861455483649364)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 2.5142809312352178e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (0.93399061278203799, 0.91464011169195503, 0.92431536223699651)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 2.0308198270606837e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.2840499491339037, 1.2795109547441923, 1.2817804519390479)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.6054802255338307e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (1.144581104779016, 1.1387446071584701, 1.1416628559687432)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 2.7566382059299685e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (1.2461558789105278, 1.2418819413372433, 1.2440189101238857)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 2.7071006571706039e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.4009121502981356, 2.2897106604268016, 2.3453114053624686)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',2.0,3.0,'natural','taper=0'] = 3.8083838997153489e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (2.2311855641632823, 2.2276349426741713, 2.2294102534187266)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 3.9253762783558608e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (2.2540765959285429, 2.2505674693406141, 2.2523220326345785)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 3.8724712947310538e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4302478809429666, 3.201306915031719, 3.3157773979873428)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',3.0,4.0,'natural','taper=0'] = 4.7404423341303804e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (3.2494206183121292, 3.2401747996074373, 3.2447977089597835)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 4.6008933865806358e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (3.2577804247553663, 3.2487921817713339, 3.2532863032633501)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 4.5878942702529201e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = (809.42748080722106, 763.39914092327945, 786.4133108652502)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.3283934944267752e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (809.24983228930887, 763.28880739402848, 786.26931984166868)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 1.3281105060460254e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (809.24995521868073, 763.28894751672385, 786.26945136770223)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 1.3281107150314472e-05
noisestats.setdefault('freq0',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch'] = 1100000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch'] = 0.27272727272727271
noisestats.setdefault('bw',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch'] = 8.9540351172688594e-07
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.5891378560443129, 0.52331942699432932, 0.55622864151932117)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = 1.6393637199423332e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (0.53735737651290916, 0.50281178016087991, 0.52008457833689459)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 2.4122957252720664e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (0.87680719810140784, 0.86713141934541871, 0.87196930872341327)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 2.3182770290901695e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.3762001837427291, 1.2892319201560507, 1.3327160519493899)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.8248545891717183e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (1.1634585466663963, 1.1578832932974259, 1.1606709199819112)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 3.4455440106773922e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (1.2633219237375239, 1.257809651443488, 1.2605657875905059)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 3.1794141463923434e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.3760970496147213, 2.2604501292170065, 2.3182735894158641)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = 4.0258699667161159e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (2.2354185437639762, 2.214346067885121, 2.2248823058245488)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 4.0992196711930468e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (2.2578514754377723, 2.2383721158558658, 2.2481117956468193)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 4.050177218544737e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4047771481541185, 3.2807187421957504, 3.3427479451749345)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = 5.3030353007899612e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (3.2476043988884871, 3.251824160679484, 3.2497142797839853)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 5.1311068282252249e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (3.256458396575824, 3.2604600960527867, 3.2584592463143052)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 5.1034029759251374e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = (766.36687801683058, 738.03274638284586, 752.19981219983822)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.8920192347795076e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (766.42682095654334, 735.21606066907873, 750.82144081281103)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 1.8962918357287845e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (766.42693523184482, 735.21612088551217, 750.8215280586785)
noisestats.setdefault('freq0',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch'] = 650000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch'] = 0.46153846153846156
noisestats.setdefault('bw',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 1.8962920552802283e-05
noisestats.setdefault('pixnoise0',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch'] = 9.0804419670095359e-07
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.84941278022712852, 0.7150139051701927, 0.78221334269866061)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',0.4,1.0,'natural','taper=0'] = 1.9894206683170711e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (0.79553814166776238, 0.71305266492787356, 0.75429540329781797)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 2.5934806301497868e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.0224822651094836, 0.97361309446865507, 0.99804767978906939)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 2.0631433255940633e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.2317700529878013, 1.2155835637314696, 1.2236768083596354)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.1750222735896727e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (1.1569469121940184, 1.1396500093736615, 1.14829846078384)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 2.4038007572065349e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.2542280965066634, 1.2403710514794017, 1.2472995739930326)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 2.4363015838014598e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.4231037826962991, 2.3135649653034998, 2.3683343739998994)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',2.0,3.0,'natural','taper=0'] = 3.704904095381873e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (2.24607543493868, 2.2316736372252413, 2.2388745360819606)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 4.2695085512343356e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (2.2679639681965011, 2.2544836504507706, 2.2612238093236359)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 4.2042186967097395e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4511897665175546, 3.2502340172661999, 3.3507118918918772)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',3.0,4.0,'natural','taper=0'] = 4.4950816389712555e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (3.2510562492178803, 3.2519148308332433, 3.2514855400255618)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 4.645338043436611e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (3.2593335550767577, 3.2601716239708947, 3.259752589523826)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 4.6308497677231616e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = (800.74721583165774, 785.00516550977693, 792.87619067071728)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.0670243009481176e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (743.48288012985734, 721.42462870510951, 732.45375441748342)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 1.0503264247022512e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (743.48315631965988, 721.42486852408933, 732.45401242187461)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-30_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 1.050326490766415e-05
noisestats.setdefault('freq0',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch'] = 800000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch'] = 0.375
noisestats.setdefault('bw',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch'] = 9.0398790444029122e-07
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.72354990704057365, 0.68300866408739902, 0.70327928556398633)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',0.4,1.0,'natural','taper=0'] = 1.8069029676013088e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (0.66382055337193724, 0.61922869115693691, 0.64152462226443707)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 2.7092615501914778e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (0.94723830483392579, 0.92005060430056962, 0.93364445456724776)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',0.4,1.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 2.2599431262735253e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.3150141096457786, 1.2423684672270612, 1.2786912884364199)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.5274419165414829e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (1.1494330690783379, 1.1470985099288935, 1.1482657895036157)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 2.9214367465807023e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (1.248606705666369, 1.2466144853292969, 1.2476105954978329)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',1.0,2.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 2.9057731478039205e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.3329067856610375, 2.3636429658508731, 2.3482748757559553)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',2.0,3.0,'natural','taper=0'] = 3.8123401503044775e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (2.2504309930080679, 2.2213948573234816, 2.235912925165775)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 4.5642850933717294e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (2.271084846651096, 2.244275847204003, 2.2576803469275495)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',2.0,3.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 4.5041686847183605e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.4279327780009647, 3.2096771161092623, 3.3188049470551135)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',3.0,4.0,'natural','taper=0'] = 4.7839341976369733e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (3.2478545242002266, 3.2481511114979504, 3.2480028178490885)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 5.2263378357423595e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (3.2560803576601076, 3.2563965952426779, 3.2562384764513927)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',3.0,4.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 5.2115782749695037e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = (803.31705835157732, 777.45163584393993, 790.38434709775856)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.2472263574063335e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = (803.10159449236153, 777.27949882387486, 790.19054665811814)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=0'] = 1.2469119266492128e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = (803.10176676914637, 777.27965663897851, 790.19071170406244)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-10_800MHz_1ch',600.0,3600.0,'robust=-2.0','fov=12.500000arcmin','taper=1.0'] = 1.2469119266492128e-05
noisestats.setdefault('freq0',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch'] = 1100000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch'] = 0.27272727272727271
noisestats.setdefault('bw',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch'] = 8.8816998983935481e-07
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.5874543382133175, 0.5334444385667233, 0.56044938839002034)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'natural','taper=0'] = 1.6417612321972554e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (0.53219995690862676, 0.5095782019822549, 0.52088907944544083)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 2.3725879912907166e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (0.87536449320453913, 0.86981604967073101, 0.87259027143763501)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',0.4,1.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 2.2495451447871194e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.3590628760761603, 1.3032731150688437, 1.331167995572502)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.8061413733345265e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (1.1584655016570715, 1.1593752210402746, 1.1589203613486729)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 3.3570285376598224e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (1.25963839918944, 1.260080215132686, 1.2598593071610629)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',1.0,2.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 3.0649388706760435e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.3870122712983779, 2.2434697553261724, 2.3152410133122752)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'natural','taper=0'] = 3.9859474664073613e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (2.2317690397516747, 2.2190951816159945, 2.2254321106838346)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 3.9508611441158218e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (2.2545885430136692, 2.2429233904711676, 2.2487559667424186)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',2.0,3.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 3.9018010182951187e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.3086322884633796, 3.3769536524305672, 3.3427929704469737)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'natural','taper=0'] = 5.3691692280119855e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (3.2534428046485822, 3.2365436577491526, 3.2449932311988672)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 5.0064689692728418e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (3.262020952211349, 3.2455226577941838, 3.2537718050027662)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',3.0,4.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 4.9774777000713687e-06
noisestats.setdefault('freq0',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch'] = 650000000.0
noisestats.setdefault('wavelength',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch'] = 0.46153846153846156
noisestats.setdefault('bw',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch'] = 50000000.0
noisestats.setdefault('synthesis_time',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch'] = 28740.0
noisestats.setdefault('integration',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch'] = 60.0
noisestats.setdefault('vis_noise',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch'] = 0.0051639777949432225
noisestats.setdefault('pixnoise0',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch'] = 8.7031720872064368e-07
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = (768.02594462947184, 745.19120944500082, 756.60857703723627)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.911343388563609e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = (768.04579199377088, 744.36002771701692, 756.20290985539395)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=0'] = 1.9124385042920855e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = (768.04591534156555, 744.36013644131992, 756.20302589144273)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_1100MHz_1ch',600.0,3600.0,'robust=-2.0','fov=9.090909arcmin','taper=1.0'] = 1.9124385042920855e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',0.4,1.0,'natural','taper=0'] = (0.84321728308925792, 0.72801533168847732, 0.78561630738886756)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',0.4,1.0,'natural','taper=0'] = 2.0161479660893397e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (0.7917769923909902, 0.73149660075552603, 0.76163679657325811)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 2.5741020564197572e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.0189658071075509, 0.98633436314040135, 1.0026500851239761)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',0.4,1.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 2.0285858299148317e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',1.0,2.0,'natural','taper=0'] = (1.2169828494942363, 1.225989368435104, 1.2214861089646702)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',1.0,2.0,'natural','taper=0'] = 2.1596835359707408e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (1.1556305155794515, 1.137652558169219, 1.1466415368743352)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 2.3381257126856916e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (1.2530737571228354, 1.2395269969856093, 1.2463003770542223)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',1.0,2.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 2.3650948242814262e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',2.0,3.0,'natural','taper=0'] = (2.4002756735483457, 2.3007440525300158, 2.3505098630391807)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',2.0,3.0,'natural','taper=0'] = 3.640986041557966e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (2.2405001113834282, 2.2350622281072168, 2.2377811697453227)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 4.0006259613643342e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (2.2629453044667303, 2.2578312340893918, 2.260388269278061)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',2.0,3.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 3.9401745395946612e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',3.0,4.0,'natural','taper=0'] = (3.3820904342442568, 3.293099362973591, 3.3375948986089239)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',3.0,4.0,'natural','taper=0'] = 4.5504209417640001e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (3.2643141162927698, 3.2412103087957331, 3.2527622125442512)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 4.5117250952900008e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (3.2725843599884468, 3.2497727645448968, 3.2611785622666716)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',3.0,4.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 4.4946418662908789e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = (800.11748334383196, 793.24263817642964, 796.6800607601308)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'natural','taper=0'] = 1.0591380637238289e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = (733.72272901956148, 749.18642882699783, 741.45457892327966)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=0'] = 1.0242853512156741e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = (733.72301226116269, 749.18663430342644, 741.45482328229457)
noisestats.setdefault('pixnoise',{})['SKA1W9-12A72B120_8h60s_dec-50_650MHz_1ch',600.0,3600.0,'robust=-2.0','fov=15.384615arcmin','taper=1.0'] = 1.0242853173437944e-05
