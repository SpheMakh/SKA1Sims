# auto-generated noise stats file
settings = dict(MKLO_NCHAN=1,MKLO_BW=50000.0,XWEIGHTS='uniform',MEASURE_NOISE=True,LOG_DISABLE=None,SCWEIGHT='uniform',NPIX_PSF=1024,MEASURE_PSF=False,LOG_FLUSH=None,SEFD=400,OUTDIR='FULL-26May',_SEFD={'ASKAP': {'1': 1525, '3': 1220, '2': 915}, 'MKT': {'2': 551, '1b': 831}, 'MID': {'1': 673, '3': 400, '2': 400, '5': 528, '4': 441}, 'SUR': {'1': 976, '3': 781, '2': 586}},ARCSEC=4.84813681109536e-06,OUTFILE='FULL-26May/plots-SKA1V8_8h60s_dec-10_650MHz_1ch/SKA1V8_8h60s_dec-10_650MHz_1ch',FOVNORM=1000000000.0,SIDELOBES_R1_ARCSEC=1800,JOBS=6,LABEL='',WAVELENGTH=0.21,SCWEIGHTFOV='512arcsec',BASEFREQ=1400000000.0,LSM=None,BANDWIDTH=None,DOALL=True,SIMSCRIPT='turbo-sim.py',CELLSIZE_PSF='.05arcsec',FOV=120,SIDELOBES_CELL_ARCSEC=0.5,MKLO_BASE='SKA1V8',ARCMIN=0.0002908882086657216,VERBOSE=1,PYXIS_LOAD_CONFIG=True,SUFFIX='spw0',MS='MS/SKA1V8_8h60s_dec-10_650MHz_1ch.MS',TAPER=0,SKIPNOISE=False,NO_X11=True,QUIET=None,MAKEMS_OUT='MS',MAKEMS_REDO=False,RFI=False,RESBINS=((0.4, 1), (0.4, 2), (1, 2), (2, 3), (3, 4), (3, 10), (600, 3600)),XWEIGHTS0='natural',MSLIST='FULL-26May/mslist.txt',FILLIMAGE='SimsCont_Cosm/toycube/im0.fits',LEGACY_ANTS=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63],PYXIS_AUTO_IMPORT_MODULES=False,SKIPFILL=False,UVSTEP=0,XW=False,MKLO_NBAND=1,SCTAPER=1,JOB_STAGGER=10,XFOVS=(10, 120),LOG='FULL-26May/plots-SKA1V8_8h60s_dec-10_650MHz_1ch/log-SKA1V8_8h60s_dec-10_650MHz_1ch.txt',SIMJOB='simulate',STEP=1,WEIGHTS='natural:briggs,robust=-2,fov=10:briggs,robust=-2,fov=10,taper=1',STATSFILE='FULL-26May/genstats.py',PERSIST=None,FWHM=2.3548200450309493,MEASURE_SIDELOBES=False,CUBE_IMAGE='SKA1V8_8h60s_dec-10_650MHz_1ch.1chan.fits',UVBINS=None,SCROBUST='',DEG=0.017453292519943295,XTAPERS=('', ',taper=1', ',taper=3'),UVFRACBINS=None,STATQUALS=('SKA1V8_8h60s_dec-10_650MHz_1ch',),INTEGRATION=None,MIXED=False,FILLIMAGE_SPWIDS=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],LOG_HEADER='## Mon May 26 12:52:10 2014:\n/home/makhathini/meqtrees/pyxis/Pyxis/bin/pyxis -j6 OUTDIR=FULL-26May per_noise_full',SKA_ONLY=False,SIDELOBES_R0_ARCSEC=900,DESTDIR='FULL-26May/plots-SKA1V8_8h60s_dec-10_650MHz_1ch')
noisestats = {}
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (13.035902805581406, 13.422179170994035, 13.229040988287721)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (8.2926093876044931, 10.319312651733089, 9.305961019668791)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (6.5966438660586979, 6.9187297663961962, 6.757686816227447)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (11.062807069713218, 10.785339635934777, 10.924073352823997)
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (11.685485645021027, 12.035470926280659, 11.860478285650842)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (7.5272861635934669, 5.8045091345339621, 6.6658976490637141)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (0.0010710334363201405, 0.0010689217782636877)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = 4.1541889555112587e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (0.001388903325382398, 0.0012684075909560944)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (1.7737724602320608, 1.3517376280875852, 1.562755044159823)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (0.0008519086141072506, 0.00047794176521712167)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = 4.2487546251699266e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (0.0008449364132112398, 0.00046776212633252651)
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (2.6470634328498348, 1.7787522426786582, 2.2129078377642464)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (0.0008358697272188606, 0.00047504086480648817)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0014709956538194158, 0.0014709973523059383)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = (0.000831713600853742, 0.00046669247217284422)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = 1.0575898288763663e-06
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 1.3580751053111027e-05
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = 1.0806597993111148e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0017086578114839863, 0.0017086350003882942)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.9252403431943041, 1.5354626190902172, 1.7303514811422607)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 1.6278597911533627e-05
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = 1.0545311370830971e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (2.7509264213386286, 1.9093557589446439, 2.3301410901416362)
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-10_650MHz_1ch','natural','taper=0'] = 1.0708827719673966e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0013074383481259148, 0.0013074366760312652)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 1.2340317494350696e-05
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0015754926137738834, 0.0015755183833448146)
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.78168237785936012, 0.70024105081912102, 0.74096171433924063)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (5.360074746112212, 5.6215180839932835, 5.4907964150527473)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.79552632952948665, 0.74694311036926431, 0.77123471994937542)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 1.4961448545570828e-05
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (9.4944450511456022, 9.7787765417942367, 9.6366107964699204)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.90429604054954627, 0.86057937533485707, 0.88243770794220167)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.78282431872351033, 0.70063949546407034, 0.74173190709379033)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (0.0009729337554011712, 0.00096685860891459531)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = 4.0352725139378966e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (0.0012756575775484703, 0.0011396870366614702)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (1.4845566900321239, 1.1263845042246934, 1.3054705971284086)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = 4.4341800393755854e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (2.2033135585760961, 1.4769146935422399, 1.840114126059168)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0013794772382480424, 0.0013794719858451572)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0007395810787330319, 0.00073958141655497411)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0007248892103426618, 0.00072488821941887015)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0015855392614475996, 0.0015855342189301036)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 1.2499906702933564e-05
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 1.4719930618445492e-05
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.6699798781821387, 1.3475963345761839, 1.5087881063791613)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0008057063703993711, 0.00080570834726251348)
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (2.3284461618212093, 1.6328343182539753, 1.9806402400375922)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0007258156914736514, 0.00072581603570252005)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0012165978794332094, 0.0012165896648005442)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0014364372015127518, 0.0014364314616447014)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 5.0808668168403073e-06
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 1.1414660903230646e-05
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.1656198366167788e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (4.2879643930893865, 4.497128981891886, 4.3925466874906363)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 1.3390669850274028e-05
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (7.5955790422475777, 7.8232462940302758, 7.7094126681389268)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.8798770144376716e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 3.9830344130328251e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (0.0008684920709159116, 0.0008527476016873196)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = 3.1230719097502025e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (0.001142899457330759, 0.0010307650810997863)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = 3.06735540103759e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (1.2315598601231632, 0.92334080878833324, 1.0774503344557482)
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.0924245146646592, 1.0201569480256998, 1.0562907313451795)
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (1.8093301848339989, 1.2087367338921495, 1.5090334593630743)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.0880574367739133, 1.0401178549780816, 1.0640876458759974)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.1645383577989799, 1.1233883153553497, 1.1439633365771646)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.001288087860374081, 0.0012880879088658758)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.0691595816587098, 1.0111241604085661, 1.0401418710336379)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0014954225238928225, 0.0014954180128780746)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 7.7530527431611994e-06
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 8.8246921989247324e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.4607354902481833, 1.1932556199053965, 1.32699555507679)
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.9615619748469448, 1.3983796537286264, 1.6799708142877856)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.001148150813743199, 0.00114814820244453)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0013183555869177165, 0.0013183512280896825)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0006039046318642884, 0.00060390533001456631)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 7.2105216740921566e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005241840878461323, 0.00052418438574565408)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 8.0616586071921932e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (3.0632761192145814, 3.2123804575380417, 3.1378282883763116)
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (5.425640728773498, 5.5880580406828191, 5.5068493847281585)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005987356662551198, 0.0005987339449288647)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.00050414355257922, 0.00050414407913967451)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (0.0007768675049577592, 0.00077534734465815338)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (0.0010761271598778177, 0.00090506961312596167)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = 3.0622471156869577e-06
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = 3.3131957339119923e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.93591672614883903, 0.70171502756398851, 0.81881587685641377)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 4.3712083158194014e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (1.3460083507671523, 0.89191422374693474, 1.1189612872570436)
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.654922849900674e-06
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 4.0819637898317473e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.001151403851140787, 0.0011514036883958968)
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-10_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.4804896523930797e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0013586361995944333, 0.0013586264990842029)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 7.8512059590779444e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (10.591855899739764, 10.906449485896484, 10.749152692818125)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 8.0826330809598578e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.2505836736118061, 1.0558151649336103, 1.1531994192727082)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (9.4709873971468888, 8.3846305407633483, 8.9278089689551194)
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.5482908285969517, 1.1565698997184441, 1.3524303641576978)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (8.9906128070369249, 8.7645942657243321, 8.8776035363806294)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (6.1159804436232292, 4.7169136016970716, 5.4164470226601509)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.001051544336404093, 0.0010515407130001822)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0011840562425661694, 0.0011840547127484012)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 7.1445648761780915e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (6.5966289150696236, 6.5210011740956402, 6.5588150445826319)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 7.2864147529610533e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (11.685475860447079, 10.89446921226132, 11.289972536354199)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (0.0007487454054327789, 0.0005267980442068865)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (0.0007387084764155722, 0.00051566045623263222)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (0.0007279918287722122, 0.00050271063387747044)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (0.0008732369217075758, 0.0008659324164881914)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (0.0011486736610613602, 0.0010245302027388167)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = 4.0391437513483347e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = (0.0007269061641346134, 0.00049840091409833844)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = 4.3722939685191835e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (1.6174071979341946, 1.2996829580338403, 1.4585450779840174)
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (2.4690911638444661, 1.731485905318086, 2.1002885345812761)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = 1.1017870303551498e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = 1.1078567445266184e-06
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = 1.172512004588342e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-10_800MHz_1ch','natural','taper=0'] = 1.1148189915860793e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0015051226445046827, 0.0015051294503916259)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0017824475533923009, 0.0017824340969622644)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 1.3825993250311421e-05
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 1.7106427586854258e-05
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.7571593710551283, 1.4831529108756107, 1.6201561409653695)
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (2.5648660012433062, 1.8701326514458221, 2.2174993263445639)
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.67600565987839056, 0.60488656684731557, 0.64044611336285306)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.67869511679433314, 0.64623567248981773, 0.66246539464207543)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.76595337270454011, 0.73223114881313511, 0.74909226075883761)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.66300624267355102, 0.62023088991262354, 0.64161856629308733)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0013076975924770126, 0.0013076963028313311)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0016053592941686538, 0.0016053712000437866)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 1.2316388902211411e-05
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 1.5583955749852707e-05
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (5.3600642721450242, 5.2982483857547669, 5.329156328949896)
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (9.4944302875872157, 8.8521984386197357, 9.1733143631034757)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (0.0010636398244278432, 0.00093559068298820379)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (0.0008058913605223938, 0.00078724740451225749)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = 4.4917391363820866e-06
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = 4.270294679400375e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (2.0582852961504128, 1.4436555583476565, 1.7509704272490345)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (1.3552268332520274, 1.082855953624984, 1.2190413934385056)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0007205488765914484, 0.00072054848650313454)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006696117703619922, 0.00066961167708152645)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0007479365695547211, 0.00074793698711470198)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006598950925113936, 0.00065989454825081471)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0016562411314311734, 0.0016562450535704662)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0014041891835878061, 0.0014041841125859878)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 1.5394488900403843e-05
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 1.264615678184935e-05
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (2.1737422319786255, 1.6097387240058347, 1.8917404779922302)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.5289441524977463, 1.2990845657935794, 1.4140143591456629)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 5.1606179739449788e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.1322556993475314e-06
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.6870235139533502e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.005238245928941e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0014735257529641345, 0.0014735047277320442)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0011964930123192716, 0.0011964862257830492)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 1.3880706097071142e-05
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 1.1238739018329566e-05
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (7.5955703195423743, 7.0817239408242676, 7.3386471301833209)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (4.2879569559933985, 4.2387776580671312, 4.2633673070302649)
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.0288364410824669, 0.97708644048789639, 1.0029614407851817)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.0124526941907064, 0.97626977458532582, 0.99436123438801616)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.0629598393294371, 1.0324968366329901, 1.0477283379812135)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (0.0009633874758925922, 0.00083270238053117964)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (0.0007352828943737932, 0.00070715744987018064)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = 3.2531133525729775e-06
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = 3.1777045601664666e-06
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.99882491032736342, 0.96196013815527426, 0.98039252424131884)
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (1.6888698524873249, 1.1877791133922, 1.4383244829397626)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (1.1233327883137367, 0.8934167855707561, 1.0083747869422464)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0015357399117970408, 0.001535732346776757)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0012824796985569794, 0.0012824765815070652)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 8.8505512453865482e-06
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 7.6422852781360604e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.8305859174736712, 1.3925949523754615, 1.6115904349245662)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.3483532466698676, 1.1499356652694341, 1.2491444559696507)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005970185045703834, 0.00059701717062935096)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005616494204260211, 0.0005616471127893476)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005191166598470856, 0.00051911765251119681)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0004946382644681088, 0.00049463793298950751)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0013315888338291085, 0.0013315992472850929)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0010882865656094006, 0.0010882824905903083)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 7.9109181882375075e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (5.425637841024348, 5.058941608709226, 5.2422897248667866)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 6.77250655549792e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (3.0632693610526509, 3.0278026314173907, 3.0455359962350208)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 4.4875582802413691e-06
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 4.000429313029989e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (0.0009709132304790395, 0.0007481337989402796)
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.8455054562708872e-06
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = 3.1548063868375618e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (0.0006661188683863009, 0.00066537737116904047)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = 3.0992927873869987e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-10_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.7449724475394425e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (1.2543837712308552, 0.88750170772613035, 1.0709427394784927)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.85878077074385195, 0.68787109886574838, 0.77332593480480016)
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (8.4745285332972582, 8.7236438490229187, 8.5990861911600884)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (7.1925378123177817, 7.0112843022055769, 7.1019110572616793)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0013654603334354355, 0.0013654552100915991)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (5.3907392914921095, 6.7077384612338529, 6.0492388763629812)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0011260348625086883, 0.0011260338640396207)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (4.8927189953237775, 6.2794044145226469, 5.5860617049232122)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 8.1403619755354305e-06
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 7.4161541169498749e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.4483163451065246, 1.1781021804602323, 1.3132092627833785)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.1835988173990197, 1.0146604728369555, 1.0991296451179875)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0011641441539298094, 0.0011641173799746131)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (0.0006588728660547728, 0.00051574887318770011)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0009773773720688538, 0.00097737785137459472)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 7.1922452963494709e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (0.0006144139094642159, 0.0004776742681563426)
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (11.685494298285928, 11.190221886867906, 11.437858092576917)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 6.4604286275156125e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (0.0006363615749520671, 0.00049674403733013337)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (6.5966202061331609, 7.0679193853804207, 6.8322697957567904)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = (0.0006149911468244459, 0.00047563801567138272)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = 1.180413338299873e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (0.0010846992921890257, 0.00092810430868362067)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = 1.205952022119835e-06
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = 4.1921501300213507e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (0.0007643177804544808, 0.00075888239997026676)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = 4.092986300701934e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (2.3662822103535932, 1.8511727910732136, 2.1087275007134032)
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = 1.1634884832633826e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-10_1000MHz_1ch','natural','taper=0'] = 1.1287044631005181e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (1.512731335344127, 1.3744658903154536, 1.4435986128297902)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.001861871442565239, 0.0018618790914482458)
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.59655566283072059, 0.56473336380163319, 0.58064451331617684)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 1.7289488465588656e-05
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0015318616526539001, 0.001531862957454065)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.66038220115808766, 0.62678773369493013, 0.64358496742650884)
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (2.4514200350601953, 1.9771665325093881, 2.2142932837847917)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 1.3991210900711314e-05
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.61288802175296619, 0.58747367246303539, 0.60018084710800079)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.6487379764614769, 1.5407667043418409, 1.594752340401659)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.60148432472883517, 0.57742081339977247, 0.58945256906430377)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0016844143537692135, 0.0016844315597955336)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.00131781597765094, 0.001317816830812638)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 1.5698372433691357e-05
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (9.4944298578937847, 9.0920945528501651, 9.293262205371974)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 1.2238882696077307e-05
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (5.3600558826604576, 5.7426925415290233, 5.5513742120947409)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0007201447619147114, 0.00072014430655627335)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (0.0009931166256017285, 0.00084519869439570133)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006847609044062491, 0.00068476060795160895)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = 4.4358574531707304e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (0.0007390551562213234, 0.00071549919606636863)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = 4.1450722766875266e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (1.9700269129508441, 1.545930527125644, 1.7579787200382442)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0005938216468607726, 0.00059382183093615454)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (1.2706542254074458, 1.1476488260930049, 1.2091515257502254)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.000572775631868414, 0.00057277729489209762)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0017031270766372428, 0.0017031168810370592)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 5.3924495516974309e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.001416361035729026, 0.0014163607270281436)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 1.540020140592028e-05
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.9368326551399056e-06
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 1.2864094655813983e-05
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (2.073608600486808, 1.6972375527631207, 1.8854230766249644)
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.8926696181921319e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.4395529475703128, 1.3391461406126628, 1.3893495440914878)
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.6670216219608555e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0015175199154499742, 0.0015175295469478671)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0011888040319686173, 0.0011888063963393053)
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.99364571814057279, 0.96308375922038492, 0.9783647386804788)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 1.3738572129609972e-05
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (7.595574616559448, 7.2739566925005299, 7.4347656545299889)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 1.1198194753232377e-05
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.99226070975763303, 0.97266383294925551, 0.98246227135344433)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (4.2879542990494475, 4.5941297256000304, 4.4410420123247389)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.95998230833891407, 0.93511522390499324, 0.94754876612195371)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.95028734201848619, 0.92972402368066631, 0.9400056828495762)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (0.0009033092739482019, 0.00076670727849693367)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = 3.1261483052461361e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (0.0006893216070167502, 0.00065320511369978702)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = 3.1129062443521197e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (1.6179790740497126, 1.2719345819870249, 1.4449568280183689)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (1.0580192452998738, 0.94405621177749754, 1.0010377285386856)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.001566180120140494, 0.001566184905919382)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005959054321967277, 0.00059590810505306209)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 9.0959639763006268e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0012890291301468765, 0.0012890258835649112)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005410056610750864, 0.0005410062960760425)
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.7468789240519105, 1.4583911286096538, 1.6026350263307823)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 7.6065098371813683e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005398608412716854, 0.00053986266353760139)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.2702490584930721, 1.1689022984278634, 1.2195756784604677)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005163856331581414, 0.00051638539123929634)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0013596112302500067, 0.0013596217047230888)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 8.0170043201242496e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0010789220177547668, 0.0010789227124667726)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 4.5441739423885012e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (5.4256415384295842, 5.1955416977609223, 5.3105916180952537)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 6.6179766424801539e-06
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 4.0627155883136329e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (3.0632674729010723, 3.2815363594622351, 3.1724019161816539)
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 4.4141671976907667e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-10_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 4.2003079701450944e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (0.000910376314349913, 0.0006926330216173995)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = 3.1858429926341801e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (6.0546703945686779, 6.2292305701750115, 6.1419504823718452)
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (0.0006248292058341226, 0.00062331062591428792)
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (1.2100973148471612, 0.95231064064169801, 1.0812039777444296)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (5.1342119142318765, 5.0085169185764755, 5.071364416404176)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = 3.0331843722672614e-06
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.82198884903944858, 0.72153335293217624, 0.77176110098581241)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (3.8528291914635826, 2.891036393630146, 3.3719327925468643)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (3.4947777940934865, 2.6953138070333775, 3.0950458005634323)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0013729125179814028, 0.001372904055744646)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 8.0107913593150032e-06
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.00112526533495765, 0.0011252680548666186)
noisestats.setdefault('psf_fwhm',{})['SKASUR1_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.3873936127255406, 1.2106565302689776, 1.2990250714972591)
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 7.4268480901289086e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (0.0006218073982389245, 0.00062176636231077052)
noisestats.setdefault('psf_fwhm',{})['SKASUR_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.1204634137188962, 1.0088783829365622, 1.0646708983277291)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (0.0005922258566446278, 0.00059219476872918696)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (0.0006298625650853907, 0.00062979388807022859)
noisestats.setdefault('sidelobe_radius',{})['SKASUR1_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR1_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0011532150790147884, 0.0011532149706886012)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = (0.0006349077935108994, 0.0006348646773814327)
noisestats.setdefault('pixnoise',{})['SKASUR1_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 7.0230807491663379e-06
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = 7.3824620066507996e-07
noisestats.setdefault('sidelobe_radius',{})['SKASUR_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKASUR_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0009608055412396872, 0.00096080778407220012)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = 7.2228696606037598e-07
noisestats.setdefault('pixnoise',{})['SKASUR_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 6.3670050188532133e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = 7.4150916295847104e-07
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-10_1400MHz_1ch','natural','taper=0'] = 7.8024835067853778e-07
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.56718283741056141, 0.53081154959891408, 0.54899719350473775)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.57015597630086756, 0.54464987570447454, 0.55740292600267105)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.54690398112839889, 0.52078746277759547, 0.53384572195299718)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.54089728319135366, 0.51825749205174132, 0.52957738762154749)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0007211238106097738, 0.00072112398384406432)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006600335804080725, 0.00066003339113981647)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006073573049174623, 0.00060735748489051315)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0005865159571315291, 0.00058651609025170577)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 3.1997390751371389e-06
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 2.8928681187626503e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 3.3552777408844176e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 3.2412783318124279e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.97671156459070829, 0.94599959223035801, 0.96135557841053321)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.95201946882698618, 0.93457186516170143, 0.94329566699434375)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.9337211494199672, 0.91614963197532628, 0.92493539069764674)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.92345165940442653, 0.91690558924419696, 0.92017862432431174)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005861111853240077, 0.00058611081232993795)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005234990072888807, 0.00052349933540717802)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005989219575326307, 0.00059892104499264685)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005735657059276485, 0.00057356554257661054)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 2.6558105558359388e-06
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 2.352253043780891e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 2.9028580658808135e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-10_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 2.7611449544384526e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (13.035902568209456, 11.766443977585988, 12.401173272897722)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (11.06323228130014, 9.6329744653756162, 10.348103373337878)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (8.2925867980823806, 9.2164376212071932, 8.7545122096447869)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (7.5272087468146083, 7.8075847249977972, 7.6673967359062027)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (0.0008128851421172467, 0.00042510638214273252)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (0.0008009681947719706, 0.00044557220077475726)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (0.0008105628469922661, 0.00042445392618751778)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = (0.000800281964638911, 0.00043811560512334893)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = 1.0507592003431775e-06
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = 1.0990795133649896e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = 1.0852552248440031e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-30_650MHz_1ch','natural','taper=0'] = 1.1066906095374958e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.74508457873710365, 0.6699316354841155, 0.70750810711060952)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.86652678568522212, 0.80107181102169012, 0.83379929835345612)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.74999688140281684, 0.66817899596950048, 0.7090879386861586)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.76928774784118059, 0.69225146581330954, 0.73076960682724512)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.00070889334627164, 0.00070889334627163999)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0007779600429793788, 0.00077796160861479449)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006974516253544859, 0.00069745249853494335)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006908594113430264, 0.0006908580551679423)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.904984323594211e-06
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.5408574527976995e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 3.6861498083050979e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 3.5243698735748342e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.0440820206040466, 0.9914094308308703, 1.0177457257174585)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.1148513346892668, 1.0694777972965002, 1.0921645659928836)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.0498363954975347, 1.0055222761906131, 1.0276793358440739)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.0324984378576887, 0.98840534871661656, 1.0104518932871527)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005622647762085439, 0.00056226316540898872)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005444586604317571, 0.000544457685289092)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.00046661288132020956, 0.00046661341676755818)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.00044524689227081707, 0.00044524782166144045)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 4.131368145534083e-06
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.6808948077137897e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.2366564174226365e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-30_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.0894548588304338e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (10.591794555044322, 9.5625701375448369, 10.077182346294579)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (8.990811747910163, 7.8271721677080315, 8.4089919578090964)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (6.1158934378066707, 6.3431011457119997, 6.2294972917593352)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (9.4708276939101825, 7.4884799769317159, 8.4796538354209492)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (0.0007117166775517218, 0.00049661986709558577)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (0.0006822737400675599, 0.00046927947148533197)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (0.0006826833231977919, 0.00046781027920245335)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = 1.1266224236247004e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = (0.0007005652005330639, 0.00048710208448588682)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = 1.1068158055041322e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = 1.0512667368672709e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-30_800MHz_1ch','natural','taper=0'] = 1.0833383921572697e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.64263525457670057, 0.58480300137535002, 0.61371912797602524)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.73501573586495028, 0.68693267678132586, 0.71097420632313812)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.63647375850000831, 0.60136235193190524, 0.61891805521595677)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.65554508840753689, 0.61382979184941255, 0.63468744012847478)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006872887360139239, 0.00068728944034363319)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0007124453874794775, 0.00071244477377343108)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006148496756326176, 0.00061485020897232806)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006240928220144517, 0.00062409227155232015)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 5.0289107916410728e-06
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.4441337333200893e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 3.7123891651420756e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 3.8991234118702357e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.98759897845948164, 0.95683946080006288, 0.97221921962977231)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.0213465856836046, 0.98850709991879115, 1.0049268428011979)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.96828917720780294, 0.94355497913845898, 0.95592207817313102)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.97855068043462423, 0.95262881426897594, 0.96558974735180003)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005552293165784403, 0.00055522782598973488)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005087184159387435, 0.00050871820106941092)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0004464713566662325, 0.00044647098942652023)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0004698350400750906, 0.00046983588759156377)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 4.1966139271548994e-06
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.6551994280664521e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.5022084201568245e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-30_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.6346506228216803e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (8.4744979224383492, 7.6525336734439078, 8.0635157979411289)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (7.1927844955822602, 6.262260491279128, 6.7275224934306941)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (4.8926587141090119, 5.0742084942089001, 4.9834336041589555)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (5.3907353355590395, 5.9907903651281247, 5.6907628503435816)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (0.0006008437065514476, 0.00048083292609177596)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (0.0005531504719161318, 0.00043462562357438837)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = 1.1840019490854404e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (0.0005566531948165187, 0.00043654272304147256)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = 1.2505105632979333e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = (0.0005819148745748635, 0.00046418878747518774)
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = 1.1155117086327667e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-30_1000MHz_1ch','natural','taper=0'] = 1.1698112696020548e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5715791282179512, 0.55240534245519246, 0.56199223533657183)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.6349667024483775, 0.59735732420398002, 0.6161620133261787)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5877131824975167, 0.56030104719588325, 0.57400711484669997)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5956765713124178, 0.56952124835828788, 0.58259890983535279)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006945685799237977, 0.0006945687148169294)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006530104910883837, 0.000653011304129017)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0005268925052499826, 0.00052689262379728731)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0005491058561115409, 0.00054910687987537454)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.9731216272290721e-06
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.3772131283856503e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.3514916890828225e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.502236036131333e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.96211361215088709, 0.94635435451883332, 0.9542339833348602)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.96119305583076498, 0.93911306812977224, 0.95015306198026861)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.92652309222375229, 0.91157966003906854, 0.91905137613141041)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.93336133296809087, 0.91531332309167446, 0.92433732802988267)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005523773336848799, 0.00055237572232182304)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0004881097570393692, 0.0004881100769554947)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.00048411062527544644, 0.00048411362506474231)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005031303608400596, 0.0005031306867235777)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 4.1096564863413548e-06
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.5849718639152781e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (6.054664165950312, 5.4688948816435436, 5.7617795237969283)
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.9345992535474943e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-30_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 4.0757182867573324e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (5.1343694939293147, 4.4735088405977645, 4.8039391672635396)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (3.4947361551152039, 3.6239805520705515, 3.5593583535928777)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (3.8528160451669846, 4.2792165857061359, 4.0660163154365598)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (0.0005769560278525303, 0.00057516393799491824)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (0.0005420483099041283, 0.00054050140820388615)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = 7.4199648567899951e-07
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (0.0005884849608042135, 0.00058648187737231057)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = 7.2008160689386273e-07
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = (0.0005918776262113733, 0.00059035514482581051)
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = 8.0522790850457345e-07
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.55414573147298707, 0.53651815779413736, 0.54533194463356227)
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-30_1400MHz_1ch','natural','taper=0'] = 7.429964387905382e-07
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5493817871907466, 0.53082299073125494, 0.54010238896100082)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.52165600303747983, 0.51281915342442075, 0.51723757823095029)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.52589082825371858, 0.51355773525826987, 0.51972428175599417)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0007016909982580917, 0.00070169108727403961)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006331808829408832, 0.00063318090760275077)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0005774687935668377, 0.00057746876652568172)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 3.0388927170829563e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0005938701093091742, 0.00059387010930917416)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 2.6794985638456721e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 3.0770563838890754e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.94979296280907799, 0.93471122968318898, 0.94225209624613349)
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 3.1747987462506798e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.93136064656637874, 0.91680229796567347, 0.9240814722660261)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.9126245099549456, 0.90253530384854175, 0.90757990690174362)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.91997656819434015, 0.90416221753434467, 0.91206939286434241)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.000541697572114601, 0.00054169771624872748)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0004733396641906015, 0.00047333976316026044)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005470721064783773, 0.00054707153560549582)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 2.4440433953228294e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005637937323890635, 0.0005637934277214282)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 2.1262444182474188e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (13.035884684965259, 11.998728438353242, 12.51730656165925)
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 2.6114561497902292e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-30_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 2.686498157950606e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (11.063610451307296, 9.6998579365288435, 10.381734193918071)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (7.5271406217941603, 7.608498620859752, 7.5678196213269562)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (8.2925811429010601, 9.0224037742369578, 8.6574924585690098)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (0.0007924815644276169, 0.00039064056854166084)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (0.0007905115859074526, 0.00040165334035213252)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = 1.0545835707516796e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (0.0007907147449889707, 0.00039838881533550436)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = (0.0007906229486724731, 0.00038577271860076211)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = 1.1217606439301392e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = 1.0581570021066103e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.72829424831497103, 0.68199984898019805, 0.7051470486475846)
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-50_650MHz_1ch','natural','taper=0'] = 1.061889797099698e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.84470143860047464, 0.81558061471381205, 0.8301410266571434)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.73512317347326839, 0.68739679975139256, 0.71125998661233047)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.75763273000264153, 0.70832609411650638, 0.73297941205957395)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006981736409934703, 0.00069817346206462599)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.000773600899294864, 0.00077359940557575866)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006900353833986118, 0.00069003640174281392)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.7748814850390121e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006907712092128964, 0.00069077077970290549)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.4585235486213334e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 3.3937058533573723e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.0217548786696873, 0.99819850827194068, 1.0099766934708141)
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 3.513648284800341e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.0902660810254834, 1.0752637443667206, 1.0827649126961019)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.0170211439275949, 0.99490195086040667, 1.0059615473940009)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.0346281065095273, 1.0107064211954266, 1.022667263852477)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005414789053080032, 0.00054147772292942873)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005261497272956078, 0.00052614978665294152)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.948854941170625e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0004280002557872294, 0.00042800041996795272)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.00044559531286432187, 0.00044559499746858999)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.5574003789384315e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (10.591785637932293, 9.7514386179491073, 10.171612127940701)
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 2.9440039069917986e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-50_650MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.0610048407493469e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (8.9911329170982786, 7.8817989505782258, 8.4364659338382531)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (6.1158442840693317, 6.1818683577011573, 6.148856320885244)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (9.4708242272876753, 7.3309463020213803, 8.4008852646545282)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (0.0007005793098028853, 0.00047243996660649424)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (0.0006787422635367375, 0.0004507223253313082)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = 1.1595381214424957e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (0.0006829436665868598, 0.00045393758457459377)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = 1.1580288433495598e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = (0.0006911645282660609, 0.00046374608944522988)
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.63224665592284113, 0.59437619946995346, 0.61331142769639735)
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = 1.0258763352597835e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-50_800MHz_1ch','natural','taper=0'] = 1.1606984265918907e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.72049238737041688, 0.69782295987331122, 0.7091576736218641)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.63250726434289617, 0.60475540004229356, 0.61863133219259492)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.65120874742751289, 0.61958064948021119, 0.63539469845386209)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006712722724501722, 0.00067127185372632583)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0007014049316869482, 0.0007014062229435097)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.800665521530347e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006046799605669429, 0.00060468032210672553)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006093649032227277, 0.00060936441633357378)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.2209542651650007e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.96941301070017194, 0.95810375244302004, 0.96375838157159599)
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 3.4908483434023599e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 3.6313613146157406e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (1.0014806344081995, 0.99045549683794964, 0.99596806562307449)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.95808795411853387, 0.94621278811316256, 0.95215037111584822)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.96735965810097813, 0.95370184627378429, 0.96053075218738115)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005370615786210522, 0.00053706294517563875)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0004871357921009202, 0.00048713444576444187)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 4.0048975875325739e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.00042571121950780625, 0.00042571162299629215)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0004443563986656385, 0.00044435581882780098)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.4642244202584991e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (8.4744932651779958, 7.7997396768408391, 8.137116471009417)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (7.193019565303918, 6.3053091707080409, 6.7491643680059799)
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.3164500187826361e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-50_800MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.4251888105852097e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (0.0005709733202405018, 0.00043576159771461798)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (4.8926107924794531, 4.9454222222226187, 4.9190165073510359)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (5.3907251217819203, 5.8648195060169348, 5.6277723138994276)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (0.000532105940952903, 0.00040124688046579864)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = 1.1047299544823101e-06
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = 1.1863961241043313e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (0.0005393221643491738, 0.00040695618757419238)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = (0.0005535943513074162, 0.00042240403506916722)
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5672073602931561, 0.55349785300253584, 0.56035260664784592)
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = 1.0967327259606216e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-50_1000MHz_1ch','natural','taper=0'] = 1.0910285957606657e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.6234235061513389, 0.60695600374362779, 0.6151897549474834)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.58377022332752071, 0.56856958695096294, 0.57616990513924182)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.59055259514679392, 0.57744094127505785, 0.58399676821092594)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006843957118128015, 0.00068439536956721946)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006386269462447864, 0.0006386289268178535)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.7577477630423744e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0005117534920523544, 0.00051175266818544141)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0005309206968553256, 0.00053092090273907213)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.1416588195992482e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.94633812320267519, 0.94224862277677779, 0.94429337298972649)
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.0615725989768646e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 4.1941201960629636e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.94532075508096403, 0.93766811394068383, 0.94149443451082393)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.91932013985157501, 0.91251469691319953, 0.91591741838238727)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.92430124084592657, 0.91512622061713889, 0.91971373073153273)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005365977086409942, 0.00053659898907472761)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.00046693821968008984, 0.00046693932327011465)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.9743651552083849e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0004789929979928502, 0.00047899307949415652)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0004630279755401084, 0.00046302752025807373)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.4370027767988035e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (6.0546559503670956, 5.5737991701249285, 5.8142275602460121)
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (5.1345339282790388, 4.5038779731130791, 4.8192059506960589)
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.8772179123469571e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-50_1000MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 3.7590228149898502e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (0.0005119314467353261, 0.00051064366979903348)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (3.8528165216199013, 4.1891065698374916, 4.0209615457286967)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (3.4947037559505088, 3.5323948522702251, 3.5135493041103669)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = 7.6593779860360335e-07
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (0.0004827780903684379, 0.00048136935404866722)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (0.0005235548739227767, 0.00052226612716940084)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = 7.4224094000331733e-07
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = (0.0005232212559525873, 0.00052179490996042809)
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.54815056554948971, 0.53961464840618079, 0.5438826069778353)
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = 7.9360074707940899e-07
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-50_1400MHz_1ch','natural','taper=0'] = 8.0469295301930902e-07
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.54213137980087611, 0.53275777045174377, 0.53744457512630994)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.52259055662667808, 0.51511235729966098, 0.51885145696316948)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.51892510559706184, 0.51470885509353792, 0.51681698034529988)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.000676550285256939, 0.00067655040066167944)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0006072431655507903, 0.00060724321698133268)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 2.9701570700946494e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0005665137241859944, 0.00056651347610931966)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = (0.0005489670046755503, 0.0005489670615657547)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 2.6151236905138448e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.93544063578667169, 0.9289228499761979, 0.93218174288143474)
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 3.1725001477384026e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=0'] = 3.095427637851013e-06
noisestats.setdefault('psf_fwhm',{})['SKA1V8-C9B120_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.91986066099239538, 0.91237956600495995, 0.91612011349867761)
noisestats.setdefault('psf_fwhm',{})['SKA1W8_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.9127414035999768, 0.90030619328517025, 0.90652379844257358)
noisestats.setdefault('psf_fwhm',{})['SKA1W8-C9B120_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.90665416044559921, 0.89933012181328231, 0.90299214112944082)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005214359694236615, 0.00052143546032505292)
noisestats.setdefault('sidelobe_radius',{})['SKA1V8-C9B120_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1V8-C9B120_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0004518519930457159, 0.0004518513882678337)
noisestats.setdefault('pixnoise',{})['SKA1V8_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 2.3476878954971522e-06
noisestats.setdefault('sidelobe_radius',{})['SKA1W8_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005408616120509075, 0.00054086175640780869)
noisestats.setdefault('sidelobe_radius',{})['SKA1W8-C9B120_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.5, 1.0)
noisestats.setdefault('sidelobes',{})['SKA1W8-C9B120_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = (0.0005283634025641013, 0.00052836269325984221)
noisestats.setdefault('pixnoise',{})['SKA1V8-C9B120_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 2.0158349659229071e-06
noisestats.setdefault('pixnoise',{})['SKA1W8_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 2.6323809094852322e-06
noisestats.setdefault('pixnoise',{})['SKA1W8-C9B120_8h60s_dec-50_1400MHz_1ch','robust=-2.0','fov=7.142857arcmin','taper=1.0'] = 2.5459423515161972e-06
