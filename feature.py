__author__ = "Zhou Yumin"
import csv
import numpy as np

def resultHome(ch):
    if ch == 'H':
        return 3    #Win
    elif ch == 'D':
        return 1    #Draw
    else:
        return 0    #Lose

def resultAway(ch):
    if ch == 'H':
        return 0
    elif ch == 'D':
        return 1
    else:
        return 3

def getRecent(a):
    l = len(a)
    ret = sum(a[l-6:])
    return str(ret/6.0)

year = 2011
yearStr = str(year)
prevYear = str(year-1)

while year < 2015:
    lastSeasonRst = {"Arsenal": '', "Leicester": '', "Man United": '', "QPR": '', "Stoke": '', "West Brom": '',
                     "West Ham": '', "Liverpool": '', "Newcastle": '', "Burnley": '', "Aston Villa": '',
                     "Chelsea": '', "Crystal Palace": '', "Everton": '', "Southampton": '', "Swansea": '',
                     "Hull": '', "Sunderland": '', "Tottenham": '', "Man City": '', "Norwich": '', "Fulham": '',
                     "Cardiff": '', "Reading": '', "Wigan": '', "Blackburn": '', "Wolves": '', "Bolton": '',
                     "Birmingham": '', "Blackpool": '', "Brentford": '', "Yeovil": '', "Carlisle": '', "Notts County": '',
                     "Charlton": '', "Bournemouth": '', "Huddersfield": '', "Bury": '', "Milton Keynes Dons": '',
                     "Hartlepool": '', "Oldham": '', "Sheffield United": '', "Preston": '', "Colchester": '',
                     "Sheffield Weds": '', "Rochdale": '', "Stevenage": '', "Exeter": '', "Tranmere": '',
                     "Chesterfield": '', "Walsall": '', "Leyton Orient": '', "Wycombe": '', "Scunthorpe": '',
                     "Crawley Town": '', "Crewe": '', "Swindon": '', "Portsmouth": '', "Shrewsbury": '', "Doncaster": '',
                     "Coventry": '', "Bristol City": '', "Bradford": '', "Rotherham": '', "Gillingham": '',
                     "Peterboro": '', "Port Vale": '', "Barnsley": '', "Fleetwood Town": ''}

    recentHomeRst = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                     "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                     "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                     "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                     "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                     "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                     "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                     "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                     "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                     "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                     "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [], "Doncaster": [],
                     "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [], "Gillingham": [],
                     "Peterboro": [], "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}
    recentAwayRst = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                     "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                     "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                     "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                     "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                     "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                     "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                     "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                     "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                     "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                     "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [], "Doncaster": [],
                     "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [], "Gillingham": [],
                     "Peterboro": [], "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}

    recentHomeG = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                   "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                   "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                   "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                   "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                   "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                   "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                   "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                   "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                   "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                   "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [], "Doncaster": [],
                   "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [], "Gillingham": [],
                   "Peterboro": [], "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}
    recentAwayG = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                   "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                   "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                   "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                   "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                   "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                   "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                   "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                   "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                   "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                   "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [], "Doncaster": [],
                   "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [], "Gillingham": [],
                   "Peterboro": [], "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}

    recentHomeGA = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                    "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                    "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                    "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                    "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                    "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                    "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                    "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                    "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                    "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                    "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [], "Doncaster": [],
                    "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [], "Gillingham": [],
                    "Peterboro": [], "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}
    recentAwayGA = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                    "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                    "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                    "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                    "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                    "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                    "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                    "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                    "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                    "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                    "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [],
                    "Doncaster": [], "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [],
                    "Gillingham": [], "Peterboro": [], "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}

    recentHomeS = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                   "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                   "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                   "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                   "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                   "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                   "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                   "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                   "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                   "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                   "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [], "Doncaster": [],
                   "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [], "Gillingham": [],
                   "Peterboro": [], "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}
    recentAwayS = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                   "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                   "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                   "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                   "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                   "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                   "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                   "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                   "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                   "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                   "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [], "Doncaster": [],
                   "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [], "Gillingham": [],
                   "Peterboro": [], "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}
    recentHomeSA = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                    "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                    "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                    "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                    "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                    "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                    "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                    "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                    "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                    "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                    "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [], "Doncaster": [],
                    "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [], "Gillingham": [],
                    "Peterboro": [], "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}
    recentAwaySA = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                    "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                    "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                    "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                    "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                    "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                    "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                    "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                    "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                    "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                    "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [], "Doncaster": [],
                    "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [], "Gillingham": [],
                    "Peterboro": [], "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}

    recentHomeSt = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                    "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                    "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                    "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                    "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                    "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                    "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                    "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                    "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                    "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                    "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [], "Doncaster": [],
                    "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [], "Gillingham": [],
                    "Peterboro": [], "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}
    recentAwaySt = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                    "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                    "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                    "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                    "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                    "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                    "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                    "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                    "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                    "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                    "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [], "Doncaster": [],
                    "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [], "Gillingham": [],
                    "Peterboro": [], "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}
    recentHomeStA = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                     "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                     "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                     "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                     "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                     "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                     "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                     "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                     "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                     "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                     "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [], "Doncaster": [],
                     "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [], "Gillingham": [], "Peterboro": [],
                     "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}
    recentAwayStA = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                     "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                     "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                     "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                     "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                     "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                     "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                     "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                     "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                     "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                     "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [], "Doncaster": [],
                     "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [], "Gillingham": [], "Peterboro": [],
                     "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}

    recentHomeCor = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                     "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                     "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                     "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                     "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                     "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                     "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                     "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                     "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                     "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                     "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [], "Doncaster": [],
                     "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [], "Gillingham": [], "Peterboro": [],
                     "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}
    recentAwayCor = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                     "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                     "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                     "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                     "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                     "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                     "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                     "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                     "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                     "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                     "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [], "Doncaster": [],
                     "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [], "Gillingham": [], "Peterboro": [],
                     "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}
    recentHomeCorA = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                      "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                      "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                      "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                      "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                      "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                      "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                      "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                      "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                      "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                      "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [], "Doncaster": [],
                      "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [], "Gillingham": [], "Peterboro": [],
                      "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}
    recentAwayCorA = {"Arsenal": [], "Leicester": [], "Man United": [], "QPR": [], "Stoke": [], "West Brom": [],
                      "West Ham": [], "Liverpool": [], "Newcastle": [], "Burnley": [], "Aston Villa": [],
                      "Chelsea": [], "Crystal Palace": [], "Everton": [], "Southampton": [], "Swansea": [],
                      "Hull": [], "Sunderland": [], "Tottenham": [], "Man City": [], "Norwich": [], "Fulham": [],
                      "Cardiff": [], "Reading": [], "Wigan": [], "Blackburn": [], "Wolves": [], "Bolton": [],
                      "Birmingham": [], "Blackpool": [], "Brentford": [], "Yeovil": [], "Carlisle": [], "Notts County": [],
                      "Charlton": [], "Bournemouth": [], "Huddersfield": [], "Bury": [], "Milton Keynes Dons": [],
                      "Hartlepool": [], "Oldham": [], "Sheffield United": [], "Preston": [], "Colchester": [],
                      "Sheffield Weds": [], "Rochdale": [], "Stevenage": [], "Exeter": [], "Tranmere": [],
                      "Chesterfield": [], "Walsall": [], "Leyton Orient": [], "Wycombe": [], "Scunthorpe": [],
                      "Crawley Town": [], "Crewe": [], "Swindon": [], "Portsmouth": [], "Shrewsbury": [], "Doncaster": [],
                      "Coventry": [], "Bristol City": [], "Bradford": [], "Rotherham": [], "Gillingham": [], "Peterboro": [],
                      "Port Vale": [], "Barnsley": [], "Fleetwood Town": []}

    fileWrite1 = open('F:\data\Season' + yearStr + 'feature.txt', 'wb')
    fileWrite2 = open('F:\data\Season' + yearStr + 'class.txt', 'wb')
    fileWrite3 = open('F:\data\Season' + yearStr + 'odds.txt', 'wb')
    # fileWrite4 = open('F:\data\Season' + yearStr + 'finalScore.txt', 'wb')
    fin = open('F:\data\Season' + prevYear + 'finalScore.txt', 'rb')
    for line in fin:
        k, v = line.strip().split(':')
        lastSeasonRst[k] = v
    fin.close()
    lineNum = 0
    with open('F:\data\Season' + yearStr + '.csv', 'rb') as FileRead:
        lines = csv.DictReader(FileRead, dialect='excel')
        for line in lines:
            lineNum += 1
            home = line['HomeTeam']
            away = line['AwayTeam']
            oddAvH = float(line['BbAvH'])
            oddAvD = float(line['BbAvD'])
            oddAvA = float(line['BbAvA'])
            oddH = line['B365H']
            oddD = line['B365D']
            oddA = line['B365A']
            r = 1.0 / (1.0 / oddAvH + 1.0 / oddAvD + 1.0 / oddAvA)
            # print oddH
            kellyH = float(oddH) / oddAvH * r
            kellyD = float(oddD) / oddAvD * r
            kellyA = float(oddA) / oddAvA * r
            if (len(recentHomeRst[home]) >= 6) and (len(recentAwayRst[away]) >= 6):
                # print lineNum
                fileWrite1.write(lastSeasonRst[home] + ' ' + lastSeasonRst[away] + ' ')
                fileWrite1.write(getRecent(recentHomeG[home]) + ' ' + getRecent(recentAwayG[away]) + ' ')
                fileWrite1.write(getRecent(recentHomeGA[home]) + ' ' + getRecent(recentAwayGA[away]) + ' ')
                # fileWrite1.write(getRecent(recentHomeS[home]) + ' ' + getRecent(recentAwayS[away]) + ' ')
                # fileWrite1.write(getRecent(recentHomeSA[home]) + ' ' + getRecent(recentAwaySt[away]) + ' ')
                fileWrite1.write(getRecent(recentHomeSt[home]) + ' ' + getRecent(recentAwaySt[away]) + ' ')
                fileWrite1.write(getRecent(recentHomeStA[home]) + ' ' + getRecent(recentAwayStA[away]) + ' ')
                fileWrite1.write(getRecent(recentHomeCor[home]) + ' ' + getRecent(recentAwayCor[away]) + ' ')
                fileWrite1.write(getRecent(recentHomeCorA[home]) + ' ' + getRecent(recentAwayCorA[away]) + ' ')
                fileWrite1.write(str(kellyH) + ' ' + str(kellyD) + ' ' + str(kellyA) + ' ')
                fileWrite1.write(line['BbAvH'] + ' ' + line['BbAvD'] + ' ' + line['BbAvA'] + '\r\n')
                fileWrite1.write(oddH + ' ' + oddD + ' ' + oddA + '\r\n')
                fileWrite2.write(str(resultHome(line['FTR'])) + '\r\n')
                fileWrite3.write(line['BbAvH'] + ' ' + line['BbAvD'] + ' ' + line['BbAvA'] + '\r\n')

            recentHomeRst[home].append(resultHome(line['FTR']))
            recentAwayRst[away].append(resultAway(line['FTR']))

            recentHomeG[home].append(int(line['FTHG']))
            recentAwayG[away].append(int(line['FTAG']))

            recentHomeGA[home].append(int(line['FTAG']))
            recentAwayGA[away].append(int(line['FTHG']))

            recentHomeS[home].append(int(line['HS']))
            recentAwayS[away].append(int(line['AS']))

            recentHomeSA[home].append(int(line['AS']))
            recentAwaySA[away].append(int(line['HS']))

            recentHomeSt[home].append(int(line['HST']))
            recentAwaySt[away].append(int(line['AST']))

            recentHomeStA[home].append(int(line['AST']))
            recentAwayStA[away].append(int(line['HST']))

            recentHomeCor[home].append(int(line['HC']))
            recentAwayCor[away].append(int(line['AC']))

            recentHomeCorA[home].append(int(line['AC']))
            recentAwayCorA[away].append(int(line['HC']))

    fileWrite1.close()
    fileWrite2.close()
    fileWrite3.close()

    # for key in recentHomeRst:
    #     if sum(recentHomeRst[key]) > 0:
    #         fileWrite4.write(key + ':' + str(sum(recentHomeRst[key])+sum(recentAwayRst[key])) + '\r\n')
    # fileWrite4.close()

    year += 1
    yearStr = str(year)
    prevYear = str(year-1)