def fama_french_48(df):
    #create new dataframe
    ff_df = df
    #add two new columns
            #ind_code: numerical code of famafrench 48
            #ff_ind: industry name abreviation
    ff_df['ind_code'] = np.nan
    ff_df['ff_ind'] = np.nan
#Agriculture
    ff_df.loc[(ff_df.sich >= 100) & (ff_df['sich'] <= 199), ['ff_ind', 'ind_code']] = "AGRIC", 1
    ff_df.loc[(ff_df.sich >= 200) & (ff_df['sich'] <= 299), ['ff_ind', 'ind_code']] = "AGRIC", 1
    ff_df.loc[(ff_df.sich >= 700) & (ff_df['sich'] <= 799), ['ff_ind', 'ind_code']] = "AGRIC", 1
    ff_df.loc[(ff_df.sich >= 910) & (ff_df['sich'] <= 919), ['ff_ind', 'ind_code']] = "AGRIC", 1
    ff_df.loc[ff_df.sich == 2048, ['ff_ind', 'ind_code']] = "AGRIC", 1
#FOOD
    ff_df.loc[(ff_df.sich >= 2000) & (ff_df['sich'] <= 2046), ['ff_ind', 'ind_code']] = "FOOD", 2
    ff_df.loc[(ff_df.sich >= 2050) & (ff_df['sich'] <= 2063), ['ff_ind', 'ind_code']] = "FOOD", 2
    ff_df.loc[(ff_df.sich >= 2070) & (ff_df['sich'] <= 2079), ['ff_ind', 'ind_code']] = "FOOD", 2
    ff_df.loc[(ff_df.sich >= 2090) & (ff_df['sich'] <= 2092), ['ff_ind', 'ind_code']] = "FOOD", 2
    ff_df.loc[ff_df.sich == 2095, ['ff_ind', 'ind_code']] = "FOOD", 2
    ff_df.loc[(ff_df.sich >= 2098) & (ff_df['sich'] <= 2099), ['ff_ind', 'ind_code']] = "FOOD", 2
#SODA
    ff_df.loc[(ff_df.sich >= 2064) & (ff_df['sich'] <= 2068), ['ff_ind', 'ind_code']] = "SODA", 3
    ff_df.loc[(ff_df.sich >= 2086) & (ff_df['sich'] <= 2087), ['ff_ind', 'ind_code']] = "SODA", 3
    ff_df.loc[(ff_df.sich >= 2096) & (ff_df['sich'] <= 2097), ['ff_ind', 'ind_code']] = "SODA", 3
#BEER
    ff_df.loc[ff_df.sich == 2080, ['ff_ind', 'ind_code']] = "BEER", 4
    ff_df.loc[(ff_df.sich >= 2082) & (ff_df['sich'] <= 2085), ['ff_ind', 'ind_code']] = "BEER", 4
#SMOKE
    ff_df.loc[(ff_df.sich >= 2100) & (ff_df['sich'] <= 2199), ['ff_ind', 'ind_code']] = "SMOKE", 5
#TOYS
    ff_df.loc[(ff_df.sich >= 920) & (ff_df['sich'] <= 999), ['ff_ind', 'ind_code']] = "TOYS", 6
    ff_df.loc[(ff_df.sich >= 3650) & (ff_df['sich'] <= 3652), ['ff_ind', 'ind_code']] = "TOYS", 6
    ff_df.loc[ff_df.sich == 3732, ['ff_ind', 'ind_code']] = "TOYS", 6
    ff_df.loc[(ff_df.sich >= 3930) & (ff_df['sich'] <= 3931), ['ff_ind', 'ind_code']] = "TOYS", 6
    ff_df.loc[(ff_df.sich >= 3940) & (ff_df['sich'] <= 3949), ['ff_ind', 'ind_code']] = "TOYS", 6
#FUN
    ff_df.loc[(ff_df.sich >= 7800) & (ff_df['sich'] <= 7829), ['ff_ind', 'ind_code']] = "FUN", 7
    ff_df.loc[(ff_df.sich >= 7830) & (ff_df['sich'] <= 7833), ['ff_ind', 'ind_code']] = "FUN", 7
    ff_df.loc[(ff_df.sich >= 7840) & (ff_df['sich'] <= 7841), ['ff_ind', 'ind_code']] = "FUN", 7
    ff_df.loc[(ff_df.sich >= 7900) & (ff_df['sich'] <= 7911), ['ff_ind', 'ind_code']] = "FUN", 7
    ff_df.loc[(ff_df.sich >= 7920) & (ff_df['sich'] <= 7933), ['ff_ind', 'ind_code']] = "FUN", 7
    ff_df.loc[(ff_df.sich >= 7940) & (ff_df['sich'] <= 7949), ['ff_ind', 'ind_code']] = "FUN", 7
    ff_df.loc[ff_df.sich == 7980, ['ff_ind', 'ind_code']] = "FUN", 7
    ff_df.loc[(ff_df.sich >= 7990) & (ff_df['sich'] <= 7999), ['ff_ind', 'ind_code']] = "FUN", 7
#BOOKS
    ff_df.loc[(ff_df.sich >= 2700) & (ff_df['sich'] <= 2749), ['ff_ind', 'ind_code']] = "BOOKS", 8
    ff_df.loc[(ff_df.sich >= 2770) & (ff_df['sich'] <= 2771), ['ff_ind', 'ind_code']] = "BOOKS", 8
    ff_df.loc[(ff_df.sich >= 2780) & (ff_df['sich'] <= 2799), ['ff_ind', 'ind_code']] = "BOOKS", 8
#HSHLD
    ff_df.loc[ff_df.sich == 2047, ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[(ff_df.sich >= 2391) & (ff_df['sich'] <= 2392), ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[(ff_df.sich >= 2510) & (ff_df['sich'] <= 2519), ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[(ff_df.sich >= 2590) & (ff_df['sich'] <= 2599), ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[(ff_df.sich >= 2840) & (ff_df['sich'] <= 2844), ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[(ff_df.sich >= 3160) & (ff_df['sich'] <= 3161), ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[(ff_df.sich >= 3170) & (ff_df['sich'] <= 3172), ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[(ff_df.sich >= 3190) & (ff_df['sich'] <= 3199), ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[ff_df.sich == 3229, ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[ff_df.sich == 3260, ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[(ff_df.sich >= 3262) & (ff_df['sich'] <= 3263), ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[ff_df.sich == 3269, ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[(ff_df.sich >= 3230) & (ff_df['sich'] <= 3231), ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[(ff_df.sich >= 3630) & (ff_df['sich'] <= 3639), ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[(ff_df.sich >= 3750) & (ff_df['sich'] <= 3751), ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[ff_df.sich == 3800, ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[(ff_df.sich >= 3860) & (ff_df['sich'] <= 3861), ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[(ff_df.sich >= 3870) & (ff_df['sich'] <= 3873), ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[(ff_df.sich >= 3910) & (ff_df['sich'] <= 3911), ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[ff_df.sich == 3914, ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[ff_df.sich == 3915, ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[(ff_df.sich >= 3960) & (ff_df['sich'] <= 3962), ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[ff_df.sich == 3991, ['ff_ind', 'ind_code']] = "HSHLD", 9
    ff_df.loc[ff_df.sich == 3995, ['ff_ind', 'ind_code']] = "HSHLD", 9
#CLTHS
    ff_df.loc[(ff_df.sich >= 2300) & (ff_df['sich'] <= 2390), ['ff_ind', 'ind_code']] = "CLTHS", 10
    ff_df.loc[(ff_df.sich >= 3020) & (ff_df['sich'] <= 3021), ['ff_ind', 'ind_code']] = "CLTHS", 10
    ff_df.loc[(ff_df.sich >= 3100) & (ff_df['sich'] <= 3111), ['ff_ind', 'ind_code']] = "CLTHS", 10
    ff_df.loc[(ff_df.sich >= 3130) & (ff_df['sich'] <= 3131), ['ff_ind', 'ind_code']] = "CLTHS", 10
    ff_df.loc[(ff_df.sich >= 3140) & (ff_df['sich'] <= 3149), ['ff_ind', 'ind_code']] = "CLTHS", 10
    ff_df.loc[(ff_df.sich >= 3150) & (ff_df['sich'] <= 3151), ['ff_ind', 'ind_code']] = "CLTHS", 10
    ff_df.loc[(ff_df.sich >= 3963) & (ff_df['sich'] <= 3965), ['ff_ind', 'ind_code']] = "CLTHS", 10
#HLTH
    ff_df.loc[(ff_df.sich >= 8000) & (ff_df['sich'] <= 8099), ['ff_ind', 'ind_code']] = "HLTH", 11
# MEDEQ
    ff_df.loc[ff_df.sich == 3693, ['ff_ind', 'ind_code']] = "MEDEQ", 12
    ff_df.loc[(ff_df.sich >= 3840) & (ff_df['sich'] <= 3851), ['ff_ind', 'ind_code']] = "MEDEQ", 12
#DRUGS
    ff_df.loc[(ff_df.sich >= 2830) & (ff_df['sich'] <= 2831), ['ff_ind', 'ind_code']] = "DRUGS", 13
    ff_df.loc[(ff_df.sich >= 2833) & (ff_df['sich'] <= 2836), ['ff_ind', 'ind_code']] = "DRUGS", 13
#CHEMS
    ff_df.loc[(ff_df.sich >= 2800) & (ff_df['sich'] <= 2829), ['ff_ind', 'ind_code']] = "CHEMS", 14
    ff_df.loc[(ff_df.sich >= 2850) & (ff_df['sich'] <= 2879), ['ff_ind', 'ind_code']] = "CHEMS", 14
    ff_df.loc[(ff_df.sich >= 2890) & (ff_df['sich'] <= 2899), ['ff_ind', 'ind_code']] = "CHEMS", 14
#RUBBR
    ff_df.loc[ff_df.sich == 3031, ['ff_ind', 'ind_code']] = "RUBBR", 15
    ff_df.loc[ff_df.sich == 3041, ['ff_ind', 'ind_code']] = "RUBBR", 15
    ff_df.loc[(ff_df.sich >= 3050) & (ff_df['sich'] <= 3053), ['ff_ind', 'ind_code']] = "RUBBR", 15
    ff_df.loc[(ff_df.sich >= 3060) & (ff_df['sich'] <= 3099), ['ff_ind', 'ind_code']] = "RUBBR", 15
#TXTLS
    ff_df.loc[(ff_df.sich >= 2200) & (ff_df['sich'] <= 2284), ['ff_ind', 'ind_code']] = "TXTLS", 16
    ff_df.loc[(ff_df.sich >= 2297) & (ff_df['sich'] <= 2299), ['ff_ind', 'ind_code']] = "TXTLS", 16
    ff_df.loc[(ff_df.sich >= 2393) & (ff_df['sich'] <= 2395), ['ff_ind', 'ind_code']] = "TXTLS", 16
    ff_df.loc[(ff_df.sich >= 2397) & (ff_df['sich'] <= 2399), ['ff_ind', 'ind_code']] = "TXTLS", 16
#BLDMT
    ff_df.loc[(ff_df.sich >= 800) & (ff_df['sich'] <= 899), ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[(ff_df.sich >= 2400) & (ff_df['sich'] <= 2439), ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[(ff_df.sich >= 2450) & (ff_df['sich'] <= 2459), ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[(ff_df.sich >= 2490) & (ff_df['sich'] <= 2499), ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[(ff_df.sich >= 2660) & (ff_df['sich'] <= 2661), ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[(ff_df.sich >= 2950) & (ff_df['sich'] <= 2952), ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[ff_df.sich == 3200, ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[(ff_df.sich >= 3210) & (ff_df['sich'] <= 3211), ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[(ff_df.sich >= 3240) & (ff_df['sich'] <= 3241), ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[(ff_df.sich >= 3250) & (ff_df['sich'] <= 3259), ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[ff_df.sich == 3261, ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[ff_df.sich == 3264, ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[(ff_df.sich >= 3270) & (ff_df['sich'] <= 3275), ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[(ff_df.sich >= 3280) & (ff_df['sich'] <= 3281), ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[(ff_df.sich >= 3290) & (ff_df['sich'] <= 3293), ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[(ff_df.sich >= 3295) & (ff_df['sich'] <= 3299), ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[(ff_df.sich >= 3420) & (ff_df['sich'] <= 3433), ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[(ff_df.sich >= 3440) & (ff_df['sich'] <= 3442), ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[ff_df.sich == 3446, ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[(ff_df.sich >= 3448) & (ff_df['sich'] <= 3452), ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[(ff_df.sich >= 3490) & (ff_df['sich'] <= 3499), ['ff_ind', 'ind_code']] = "BLDMT", 17
    ff_df.loc[ff_df.sich == 3996, ['ff_ind', 'ind_code']] = "BLDMT", 17
#CNSTR
    ff_df.loc[(ff_df.sich >= 1500) & (ff_df['sich'] <= 1511), ['ff_ind', 'ind_code']] = "CNSTR", 18
    ff_df.loc[(ff_df.sich >= 1520) & (ff_df['sich'] <= 1549), ['ff_ind', 'ind_code']] = "CNSTR", 18
    ff_df.loc[(ff_df.sich >= 1600) & (ff_df['sich'] <= 1799), ['ff_ind', 'ind_code']] = "CNSTR", 18
#STEEL
    ff_df.loc[ff_df.sich == 3300, ['ff_ind', 'ind_code']] = "STEEL", 19
    ff_df.loc[(ff_df.sich >= 3310) & (ff_df['sich'] <= 3317), ['ff_ind', 'ind_code']] = "STEEL", 19
    ff_df.loc[(ff_df.sich >= 3320) & (ff_df['sich'] <= 3325), ['ff_ind', 'ind_code']] = "STEEL", 19
    ff_df.loc[(ff_df.sich >= 3330) & (ff_df['sich'] <= 3341), ['ff_ind', 'ind_code']] = "STEEL", 19
    ff_df.loc[(ff_df.sich >= 3350) & (ff_df['sich'] <= 3357), ['ff_ind', 'ind_code']] = "STEEL", 19
    ff_df.loc[(ff_df.sich >= 3360) & (ff_df['sich'] <= 3379), ['ff_ind', 'ind_code']] = "STEEL", 19
    ff_df.loc[(ff_df.sich >= 3390) & (ff_df['sich'] <= 3399), ['ff_ind', 'ind_code']] = "STEEL", 19
#FABPR
    ff_df.loc[ff_df.sich == 3400, ['ff_ind', 'ind_code']] = "FABPR", 20
    ff_df.loc[(ff_df.sich >= 3443) & (ff_df['sich'] <= 3444), ['ff_ind', 'ind_code']] = "FABPR", 20
    ff_df.loc[(ff_df.sich >= 3460) & (ff_df['sich'] <= 3479), ['ff_ind', 'ind_code']] = "FABPR", 20
#MACH
    ff_df.loc[(ff_df.sich >= 3510) & (ff_df['sich'] <= 3536), ['ff_ind', 'ind_code']] = "MACH", 21
    ff_df.loc[ff_df.sich == 3538, ['ff_ind', 'ind_code']] = "MACH", 21
    ff_df.loc[(ff_df.sich >= 3540) & (ff_df['sich'] <= 3569), ['ff_ind', 'ind_code']] = "MACH", 21
    ff_df.loc[(ff_df.sich >= 3580) & (ff_df['sich'] <= 3582), ['ff_ind', 'ind_code']] = "MACH", 21
    ff_df.loc[(ff_df.sich >= 3585) & (ff_df['sich'] <= 3586), ['ff_ind', 'ind_code']] = "MACH", 21
    ff_df.loc[(ff_df.sich >= 3589) & (ff_df['sich'] <= 3599), ['ff_ind', 'ind_code']] = "MACH", 21
#ELCEQ
    ff_df.loc[ff_df.sich == 3600, ['ff_ind', 'ind_code']] = "ELCEQ", 22
    ff_df.loc[(ff_df.sich >= 3610) & (ff_df['sich'] <= 3613), ['ff_ind', 'ind_code']] = "ELCEQ", 22
    ff_df.loc[(ff_df.sich >= 3620) & (ff_df['sich'] <= 3621), ['ff_ind', 'ind_code']] = "ELCEQ", 22
    ff_df.loc[(ff_df.sich >= 3623) & (ff_df['sich'] <= 3629), ['ff_ind', 'ind_code']] = "ELCEQ", 22
    ff_df.loc[(ff_df.sich >= 3640) & (ff_df['sich'] <= 3646), ['ff_ind', 'ind_code']] = "ELCEQ", 22
    ff_df.loc[(ff_df.sich >= 3648) & (ff_df['sich'] <= 3649), ['ff_ind', 'ind_code']] = "ELCEQ", 22
    ff_df.loc[ff_df.sich == 3660, ['ff_ind', 'ind_code']] = "ELCEQ", 22
    ff_df.loc[(ff_df.sich >= 3690) & (ff_df['sich'] <= 3692), ['ff_ind', 'ind_code']] = "ELCEQ", 22
    ff_df.loc[ff_df.sich == 3699, ['ff_ind', 'ind_code']] = "ELCEQ", 22
#AUTOS
    ff_df.loc[ff_df.sich == 2269, ['ff_ind', 'ind_code']] = "AUTOS", 23
    ff_df.loc[ff_df.sich == 2369, ['ff_ind', 'ind_code']] = "AUTOS", 23
    ff_df.loc[(ff_df.sich >= 3010) & (ff_df['sich'] <= 3011), ['ff_ind', 'ind_code']] = "AUTOS", 23
    ff_df.loc[ff_df.sich == 3537, ['ff_ind', 'ind_code']] = "AUTOS", 23
    ff_df.loc[ff_df.sich == 3647, ['ff_ind', 'ind_code']] = "AUTOS", 23
    ff_df.loc[ff_df.sich == 3694, ['ff_ind', 'ind_code']] = "AUTOS", 23
    ff_df.loc[ff_df.sich == 3700, ['ff_ind', 'ind_code']] = "AUTOS", 23
    ff_df.loc[(ff_df.sich >= 3710) & (ff_df['sich'] <= 3711), ['ff_ind', 'ind_code']] = "AUTOS", 23
    ff_df.loc[(ff_df.sich >= 3713) & (ff_df['sich'] <= 3716), ['ff_ind', 'ind_code']] = "AUTOS", 23
    ff_df.loc[(ff_df.sich >= 3790) & (ff_df['sich'] <= 3792), ['ff_ind', 'ind_code']] = "AUTOS", 23
    ff_df.loc[ff_df.sich == 3799, ['ff_ind', 'ind_code']] = "AUTOS", 23
#AERO
    ff_df.loc[(ff_df.sich >= 3720) & (ff_df['sich'] <= 3721), ['ff_ind', 'ind_code']] = "AERO", 24
    ff_df.loc[(ff_df.sich >= 3723) & (ff_df['sich'] <= 3725), ['ff_ind', 'ind_code']] = "AERO", 24
    ff_df.loc[(ff_df.sich >= 3728) & (ff_df['sich'] <= 3729), ['ff_ind', 'ind_code']] = "AERO", 24
#SHIPS
    ff_df.loc[(ff_df.sich >= 3730) & (ff_df['sich'] <= 3731), ['ff_ind', 'ind_code']] = "SHIPS", 25
    ff_df.loc[(ff_df.sich >= 3740) & (ff_df['sich'] <= 3743), ['ff_ind', 'ind_code']] = "SHIPS", 25
#GUNS
    ff_df.loc[(ff_df.sich >= 3760) & (ff_df['sich'] <= 3769), ['ff_ind', 'ind_code']] = "GUNS", 26
    ff_df.loc[ff_df.sich == 3795, ['ff_ind', 'ind_code']] = "GUNS", 26
    ff_df.loc[(ff_df.sich >= 3480) & (ff_df['sich'] <= 3489), ['ff_ind', 'ind_code']] = "GUNS", 26
#GOLD
    ff_df.loc[(ff_df.sich >= 1040) & (ff_df['sich'] <= 1049), ['ff_ind', 'ind_code']] = "GOLD", 27
#MINES
    ff_df.loc[(ff_df.sich >= 1000) & (ff_df['sich'] <= 1039), ['ff_ind', 'ind_code']] = "MINES", 28
    ff_df.loc[(ff_df.sich >= 1050) & (ff_df['sich'] <= 1119), ['ff_ind', 'ind_code']] = "MINES", 28
    ff_df.loc[(ff_df.sich >= 1400) & (ff_df['sich'] <= 1499), ['ff_ind', 'ind_code']] = "MINES", 28
#COAL
    ff_df.loc[(ff_df.sich >= 1200) & (ff_df['sich'] <= 1299), ['ff_ind', 'ind_code']] = "COAL", 29
#OIL
    ff_df.loc[ff_df.sich == 1300, ['ff_ind', 'ind_code']] = "OIL", 30
    ff_df.loc[(ff_df.sich >= 1310) & (ff_df['sich'] <= 1339), ['ff_ind', 'ind_code']] = "OIL", 30
    ff_df.loc[(ff_df.sich >= 1370) & (ff_df['sich'] <= 1382), ['ff_ind', 'ind_code']] = "OIL", 30
    ff_df.loc[ff_df.sich == 1389, ['ff_ind', 'ind_code']] = "OIL", 30
    ff_df.loc[(ff_df.sich >= 2900) & (ff_df['sich'] <= 2912), ['ff_ind', 'ind_code']] = "OIL", 30
    ff_df.loc[(ff_df.sich >= 2990) & (ff_df['sich'] <= 2999), ['ff_ind', 'ind_code']] = "OIL", 30
#UTIL
    ff_df.loc[ff_df.sich == 4900, ['ff_ind', 'ind_code']] = "UTIL", 31
    ff_df.loc[(ff_df.sich >= 4910) & (ff_df['sich'] <= 4911), ['ff_ind', 'ind_code']] = "UTIL", 31
    ff_df.loc[(ff_df.sich >= 4920) & (ff_df['sich'] <= 4925), ['ff_ind', 'ind_code']] = "UTIL", 31
    ff_df.loc[(ff_df.sich >= 4930) & (ff_df['sich'] <= 4932), ['ff_ind', 'ind_code']] = "UTIL", 31
    ff_df.loc[(ff_df.sich >= 4939) & (ff_df['sich'] <= 4942), ['ff_ind', 'ind_code']] = "UTIL", 31
#TELCM
    ff_df.loc[ff_df.sich == 4800, ['ff_ind', 'ind_code']] = "TELCM", 32
    ff_df.loc[(ff_df.sich >= 4810) & (ff_df['sich'] <= 4813), ['ff_ind', 'ind_code']] = "TELCM", 32
    ff_df.loc[(ff_df.sich >= 4820) & (ff_df['sich'] <= 4822), ['ff_ind', 'ind_code']] = "TELCM", 32
    ff_df.loc[(ff_df.sich >= 4830) & (ff_df['sich'] <= 4841), ['ff_ind', 'ind_code']] = "TELCM", 32
    ff_df.loc[(ff_df.sich >= 4880) & (ff_df['sich'] <= 4892), ['ff_ind', 'ind_code']] = "TELCM", 32
    ff_df.loc[ff_df.sich == 4899, ['ff_ind', 'ind_code']] = "TELCM", 32
#PERSV
    ff_df.loc[(ff_df.sich >= 7020) & (ff_df['sich'] <= 7021), ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[(ff_df.sich >= 7030) & (ff_df['sich'] <= 7033), ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[ff_df.sich == 7200, ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[(ff_df.sich >= 7210) & (ff_df['sich'] <= 7212), ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[(ff_df.sich >= 7214) & (ff_df['sich'] <= 7217), ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[(ff_df.sich >= 7219) & (ff_df['sich'] <= 7221), ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[(ff_df.sich >= 7230) & (ff_df['sich'] <= 7231), ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[(ff_df.sich >= 7240) & (ff_df['sich'] <= 7241), ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[(ff_df.sich >= 7250) & (ff_df['sich'] <= 7251), ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[(ff_df.sich >= 7260) & (ff_df['sich'] <= 7299), ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[ff_df.sich == 7395, ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[ff_df.sich == 7500, ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[(ff_df.sich >= 7520) & (ff_df['sich'] <= 7549), ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[ff_df.sich == 7600, ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[ff_df.sich == 7620, ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[(ff_df.sich >= 7622) & (ff_df['sich'] <= 7623), ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[(ff_df.sich >= 7629) & (ff_df['sich'] <= 7631), ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[(ff_df.sich >= 7640) & (ff_df['sich'] <= 7641), ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[(ff_df.sich >= 7690) & (ff_df['sich'] <= 7699), ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[(ff_df.sich >= 8100) & (ff_df['sich'] <= 8499), ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[(ff_df.sich >= 8600) & (ff_df['sich'] <= 8699), ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[(ff_df.sich >= 8800) & (ff_df['sich'] <= 8899), ['ff_ind', 'ind_code']] = "PERSV", 33
    ff_df.loc[(ff_df.sich >= 7510) & (ff_df['sich'] <= 7515), ['ff_ind', 'ind_code']] = "PERSV", 33
#BUSSV
    ff_df.loc[(ff_df.sich >= 2750) & (ff_df['sich'] <= 2759), ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[ff_df.sich == 3993, ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[ff_df.sich == 7218, ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[ff_df.sich == 7300, ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[(ff_df.sich >= 7310) & (ff_df['sich'] <= 7342), ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[ff_df.sich == 7349, ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[(ff_df.sich >= 7250) & (ff_df['sich'] <= 7253), ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[(ff_df.sich >= 7259) & (ff_df['sich'] <= 7372), ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[(ff_df.sich >= 7374) & (ff_df['sich'] <= 7385), ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[(ff_df.sich >= 7389) & (ff_df['sich'] <= 7394), ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[(ff_df.sich >= 7396) & (ff_df['sich'] <= 7397), ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[ff_df.sich == 7399, ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[ff_df.sich == 7519, ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[ff_df.sich == 8700, ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[(ff_df.sich >= 8710) & (ff_df['sich'] <= 8713), ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[(ff_df.sich >= 8720) & (ff_df['sich'] <= 8721), ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[(ff_df.sich >= 8730) & (ff_df['sich'] <= 8734), ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[(ff_df.sich >= 8740) & (ff_df['sich'] <= 8748), ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[(ff_df.sich >= 8900) & (ff_df['sich'] <= 8911), ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[(ff_df.sich >= 8920) & (ff_df['sich'] <= 8999), ['ff_ind', 'ind_code']] = "BUSSV", 34
    ff_df.loc[(ff_df.sich >= 4220) & (ff_df['sich'] <= 4229), ['ff_ind', 'ind_code']] = "BUSSV", 34
#COMPS
    ff_df.loc[(ff_df.sich >= 3570) & (ff_df['sich'] <= 3579), ['ff_ind', 'ind_code']] = "COMPS", 35
    ff_df.loc[(ff_df.sich >= 3680) & (ff_df['sich'] <= 3689), ['ff_ind', 'ind_code']] = "COMPS", 35
    ff_df.loc[ff_df.sich == 3695, ['ff_ind', 'ind_code']] = "COMPS", 35
    ff_df.loc[ff_df.sich == 7373, ['ff_ind', 'ind_code']] = "COMPS", 35
#CHIPS
    ff_df.loc[ff_df.sich == 3622, ['ff_ind', 'ind_code']] = "CHIPS", 36
    ff_df.loc[(ff_df.sich >= 3661) & (ff_df['sich'] <= 3666), ['ff_ind', 'ind_code']] = "CHIPS", 36
    ff_df.loc[(ff_df.sich >= 3669) & (ff_df['sich'] <= 3679), ['ff_ind', 'ind_code']] = "CHIPS", 36
    ff_df.loc[ff_df.sich == 3810, ['ff_ind', 'ind_code']] = "CHIPS", 36
    ff_df.loc[ff_df.sich == 3812, ['ff_ind', 'ind_code']] = "CHIPS", 36
#LABEQ
    ff_df.loc[ff_df.sich == 3811, ['ff_ind', 'ind_code']] = "LABEQ", 37
    ff_df.loc[(ff_df.sich >= 3820) & (ff_df['sich'] <= 3839), ['ff_ind', 'ind_code']] = "LABEQ", 37
#PAPER
    ff_df.loc[(ff_df.sich >= 2520) & (ff_df['sich'] <= 2549), ['ff_ind', 'ind_code']] = "PAPER", 38
    ff_df.loc[(ff_df.sich >= 2600) & (ff_df['sich'] <= 2639), ['ff_ind', 'ind_code']] = "PAPER", 38
    ff_df.loc[(ff_df.sich >= 2670) & (ff_df['sich'] <= 2699), ['ff_ind', 'ind_code']] = "PAPER", 38
    ff_df.loc[(ff_df.sich >= 2760) & (ff_df['sich'] <= 2761), ['ff_ind', 'ind_code']] = "PAPER", 38
    ff_df.loc[(ff_df.sich >= 3950) & (ff_df['sich'] <= 3955), ['ff_ind', 'ind_code']] = "PAPER", 38
#BOXES
    ff_df.loc[(ff_df.sich >= 2440) & (ff_df['sich'] <= 2449), ['ff_ind', 'ind_code']] = "BOXES", 39
    ff_df.loc[(ff_df.sich >= 2640) & (ff_df['sich'] <= 2659), ['ff_ind', 'ind_code']] = "BOXES", 39
    ff_df.loc[(ff_df.sich >= 3220) & (ff_df['sich'] <= 3221), ['ff_ind', 'ind_code']] = "BOXES", 39
    ff_df.loc[(ff_df.sich >= 3410) & (ff_df['sich'] <= 3412), ['ff_ind', 'ind_code']] = "BOXES", 39
#TRANS
    ff_df.loc[(ff_df.sich >= 4000) & (ff_df['sich'] <= 4013), ['ff_ind', 'ind_code']] = "TRANS", 40
    ff_df.loc[(ff_df.sich >= 4040) & (ff_df['sich'] <= 4049), ['ff_ind', 'ind_code']] = "TRANS", 40
    ff_df.loc[ff_df.sich == 4100, ['ff_ind', 'ind_code']] = "TRANS", 40
    ff_df.loc[(ff_df.sich >= 4110) & (ff_df['sich'] <= 4121), ['ff_ind', 'ind_code']] = "TRANS", 40
    ff_df.loc[(ff_df.sich >= 4130) & (ff_df['sich'] <= 4131), ['ff_ind', 'ind_code']] = "TRANS", 40
    ff_df.loc[(ff_df.sich >= 4140) & (ff_df['sich'] <= 4142), ['ff_ind', 'ind_code']] = "TRANS", 40
    ff_df.loc[(ff_df.sich >= 4150) & (ff_df['sich'] <= 4151), ['ff_ind', 'ind_code']] = "TRANS", 40
    ff_df.loc[(ff_df.sich >= 4170) & (ff_df['sich'] <= 4173), ['ff_ind', 'ind_code']] = "TRANS", 40
    ff_df.loc[(ff_df.sich >= 4190) & (ff_df['sich'] <= 4200), ['ff_ind', 'ind_code']] = "TRANS", 40
    ff_df.loc[(ff_df.sich >= 4210) & (ff_df['sich'] <= 4219), ['ff_ind', 'ind_code']] = "TRANS", 40
    ff_df.loc[(ff_df.sich >= 4230) & (ff_df['sich'] <= 4231), ['ff_ind', 'ind_code']] = "TRANS", 40
    ff_df.loc[(ff_df.sich >= 4240) & (ff_df['sich'] <= 4249), ['ff_ind', 'ind_code']] = "TRANS", 40
    ff_df.loc[(ff_df.sich >= 4400) & (ff_df['sich'] <= 4700), ['ff_ind', 'ind_code']] = "TRANS", 40
    ff_df.loc[(ff_df.sich >= 4710) & (ff_df['sich'] <= 4712), ['ff_ind', 'ind_code']] = "TRANS", 40
    ff_df.loc[(ff_df.sich >= 4720) & (ff_df['sich'] <= 4749), ['ff_ind', 'ind_code']] = "TRANS", 40
    ff_df.loc[ff_df.sich == 4780, ['ff_ind', 'ind_code']] = "TRANS", 40
    ff_df.loc[(ff_df.sich >= 4782) & (ff_df['sich'] <= 4785), ['ff_ind', 'ind_code']] = "TRANS", 40
    ff_df.loc[ff_df.sich == 4789, ['ff_ind', 'ind_code']] = "TRANS", 40
#WHLSL
    ff_df.loc[ff_df.sich == 5000, ['ff_ind', 'ind_code']] = "WHLSL", 41
    ff_df.loc[(ff_df.sich >= 5010) & (ff_df['sich'] <= 5015), ['ff_ind', 'ind_code']] = "WHLSL", 41
    ff_df.loc[(ff_df.sich >= 5020) & (ff_df['sich'] <= 5023), ['ff_ind', 'ind_code']] = "WHLSL", 41
    ff_df.loc[(ff_df.sich >= 5030) & (ff_df['sich'] <= 5060), ['ff_ind', 'ind_code']] = "WHLSL", 41
    ff_df.loc[(ff_df.sich >= 5063) & (ff_df['sich'] <= 5065), ['ff_ind', 'ind_code']] = "WHLSL", 41
    ff_df.loc[(ff_df.sich >= 5070) & (ff_df['sich'] <= 5078), ['ff_ind', 'ind_code']] = "WHLSL", 41
    ff_df.loc[(ff_df.sich >= 5080) & (ff_df['sich'] <= 5088), ['ff_ind', 'ind_code']] = "WHLSL", 41
    ff_df.loc[(ff_df.sich >= 5090) & (ff_df['sich'] <= 5094), ['ff_ind', 'ind_code']] = "WHLSL", 41
    ff_df.loc[(ff_df.sich >= 5099) & (ff_df['sich'] <= 5100), ['ff_ind', 'ind_code']] = "WHLSL", 41
    ff_df.loc[(ff_df.sich >= 5110) & (ff_df['sich'] <= 5113), ['ff_ind', 'ind_code']] = "WHLSL", 41
    ff_df.loc[(ff_df.sich >= 5120) & (ff_df['sich'] <= 5122), ['ff_ind', 'ind_code']] = "WHLSL", 41
    ff_df.loc[(ff_df.sich >= 5130) & (ff_df['sich'] <= 5172), ['ff_ind', 'ind_code']] = "WHLSL", 41
    ff_df.loc[(ff_df.sich >= 5180) & (ff_df['sich'] <= 5182), ['ff_ind', 'ind_code']] = "WHLSL", 41
    ff_df.loc[(ff_df.sich >= 5190) & (ff_df['sich'] <= 5199), ['ff_ind', 'ind_code']] = "WHLSL", 41
#RTAIL
    ff_df.loc[ff_df.sich == 5200, ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5210) & (ff_df['sich'] <= 5231), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5250) & (ff_df['sich'] <= 5251), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5260) & (ff_df['sich'] <= 5261), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5270) & (ff_df['sich'] <= 5271), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[ff_df.sich == 5300, ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5310) & (ff_df['sich'] <= 5311), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[ff_df.sich == 5331, ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[ff_df.sich == 5334, ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5340) & (ff_df['sich'] <= 5349), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5390) & (ff_df['sich'] <= 5400), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5410) & (ff_df['sich'] <= 5412), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5420) & (ff_df['sich'] <= 5469), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5490) & (ff_df['sich'] <= 5500), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5510) & (ff_df['sich'] <= 5579), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5590) & (ff_df['sich'] <= 5700), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5710) & (ff_df['sich'] <= 5722), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5730) & (ff_df['sich'] <= 5736), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5750) & (ff_df['sich'] <= 5799), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[ff_df.sich == 5900, ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5910) & (ff_df['sich'] <= 5912), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5920) & (ff_df['sich'] <= 5932), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5940) & (ff_df['sich'] <= 5990), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[(ff_df.sich >= 5992) & (ff_df['sich'] <= 5995), ['ff_ind', 'ind_code']] = "RTAIL", 42
    ff_df.loc[ff_df.sich == 5999, ['ff_ind', 'ind_code']] = "RTAIL", 42
#MEALS
    ff_df.loc[(ff_df.sich >= 5800) & (ff_df['sich'] <= 5829), ['ff_ind', 'ind_code']] = "MEALS", 43
    ff_df.loc[(ff_df.sich >= 5890) & (ff_df['sich'] <= 5899), ['ff_ind', 'ind_code']] = "MEALS", 43
    ff_df.loc[ff_df.sich == 7000, ['ff_ind', 'ind_code']] = "MEALS", 43
    ff_df.loc[(ff_df.sich >= 7010) & (ff_df['sich'] <= 7019), ['ff_ind', 'ind_code']] = "MEALS", 43
    ff_df.loc[(ff_df.sich >= 7040) & (ff_df['sich'] <= 7049), ['ff_ind', 'ind_code']] = "MEALS", 43
    ff_df.loc[ff_df.sich == 7213, ['ff_ind', 'ind_code']] = "MEALS", 43
#BANKS
    ff_df.loc[ff_df.sich == 6000, ['ff_ind', 'ind_code']] = "BANKS", 44
    ff_df.loc[(ff_df.sich >= 6010) & (ff_df['sich'] <= 6036), ['ff_ind', 'ind_code']] = "BANKS", 44
    ff_df.loc[(ff_df.sich >= 6040) & (ff_df['sich'] <= 6062), ['ff_ind', 'ind_code']] = "BANKS", 44
    ff_df.loc[(ff_df.sich >= 6080) & (ff_df['sich'] <= 6082), ['ff_ind', 'ind_code']] = "BANKS", 44
    ff_df.loc[(ff_df.sich >= 6090) & (ff_df['sich'] <= 6113), ['ff_ind', 'ind_code']] = "BANKS", 44
    ff_df.loc[(ff_df.sich >= 6120) & (ff_df['sich'] <= 6179), ['ff_ind', 'ind_code']] = "BANKS", 44
    ff_df.loc[(ff_df.sich >= 6190) & (ff_df['sich'] <= 6199), ['ff_ind', 'ind_code']] = "BANKS", 44
#INSUR
    ff_df.loc[ff_df.sich == 6300, ['ff_ind', 'ind_code']] = "INSUR", 45
    ff_df.loc[(ff_df.sich >= 6310) & (ff_df['sich'] <= 6331), ['ff_ind', 'ind_code']] = "INSUR", 45
    ff_df.loc[(ff_df.sich >= 6350) & (ff_df['sich'] <= 6351), ['ff_ind', 'ind_code']] = "INSUR", 45
    ff_df.loc[(ff_df.sich >= 6360) & (ff_df['sich'] <= 6361), ['ff_ind', 'ind_code']] = "INSUR", 45
    ff_df.loc[(ff_df.sich >= 6370) & (ff_df['sich'] <= 6379), ['ff_ind', 'ind_code']] = "INSUR", 45
    ff_df.loc[(ff_df.sich >= 6390) & (ff_df['sich'] <= 6411), ['ff_ind', 'ind_code']] = "INSUR", 45
#REIST
    ff_df.loc[ff_df.sich == 6500, ['ff_ind', 'ind_code']] = "REIST", 46
    ff_df.loc[ff_df.sich == 6510, ['ff_ind', 'ind_code']] = "REIST", 46
    ff_df.loc[(ff_df.sich >= 6512) & (ff_df['sich'] <= 6515), ['ff_ind', 'ind_code']] = "REIST", 46
    ff_df.loc[(ff_df.sich >= 6517) & (ff_df['sich'] <= 6532), ['ff_ind', 'ind_code']] = "REIST", 46
    ff_df.loc[(ff_df.sich >= 6540) & (ff_df['sich'] <= 6541), ['ff_ind', 'ind_code']] = "REIST", 46
    ff_df.loc[(ff_df.sich >= 6550) & (ff_df['sich'] <= 6553), ['ff_ind', 'ind_code']] = "REIST", 46
    ff_df.loc[(ff_df.sich >= 6590) & (ff_df['sich'] <= 6599), ['ff_ind', 'ind_code']] = "REIST", 46
    ff_df.loc[(ff_df.sich >= 6610) & (ff_df['sich'] <= 6611), ['ff_ind', 'ind_code']] = "REIST", 46
#FIN
    ff_df.loc[(ff_df.sich >= 6200) & (ff_df['sich'] <= 6299), ['ff_ind', 'ind_code']] = "FIN", 47
    ff_df.loc[ff_df.sich == 6700, ['ff_ind', 'ind_code']] = "FIN", 47
    ff_df.loc[(ff_df.sich >= 6710) & (ff_df['sich'] <= 6726), ['ff_ind', 'ind_code']] = "FIN", 47
    ff_df.loc[(ff_df.sich >= 6730) & (ff_df['sich'] <= 6733), ['ff_ind', 'ind_code']] = "FIN", 47
    ff_df.loc[(ff_df.sich >= 6740) & (ff_df['sich'] <= 6779), ['ff_ind', 'ind_code']] = "FIN", 47
    ff_df.loc[(ff_df.sich >= 6790) & (ff_df['sich'] <= 6795), ['ff_ind', 'ind_code']] = "FIN", 47
    ff_df.loc[(ff_df.sich >= 6798) & (ff_df['sich'] <= 6799), ['ff_ind', 'ind_code']] = "FIN", 47
#OTHER
    ff_df.loc[(ff_df.sich >= 4950) & (ff_df['sich'] <= 4961), ['ff_ind', 'ind_code']] = "OTHER", 48
    ff_df.loc[(ff_df.sich >= 4970) & (ff_df['sich'] <= 4971), ['ff_ind', 'ind_code']] = "OTHER", 48
    ff_df.loc[(ff_df.sich >= 4990) & (ff_df['sich'] <= 4991), ['ff_ind', 'ind_code']] = "OTHER", 48
    ff_df.loc[(ff_df.sich >= 3990) & (ff_df['sich'] <= 3991), ['ff_ind', 'ind_code']] = "OTHER", 48
    ff_df.loc[(ff_df.sich >= 9997) & (ff_df['sich'] <= 9998), ['ff_ind', 'ind_code']] = "OTHER", 48
    # Return dataframe
    return ff_df

df_fama = fama_french_48(df)
