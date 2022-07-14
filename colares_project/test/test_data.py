from .. import downloadData



def test_DownloadResult():
    assert downloadData()

def checkDates(df):

    dates = df.Date

    try:
        check = pd.to_datetime(dates)
    except:
        check = None
    print(check)
    return check

def checkNumFormat(df):

    prec = df.Precipitation
    temp = df.Temperature

    try:
        check_prec = prec.astype('float')
        check_temp = temp.astype('float')
    except:
        check_prec = None
        check_temp = None
    
    return None if (check_prec is None or check_temp is None) else 'Its ok'

def checkPrecRange(df):
    prec = df.Precipitation
    prec = prec.astype('float')
    prec_not_nan = prec[~prec.isnull()]
    is_in_range = ~prec_not_nan.between(0, 1000)
    sum_outside = is_in_range.sum()

    return None if sum_outside>0 else 'Its ok'

def checkPrecRange(df):
    temp = df.Temperature
    temp = temp.astype('float')
    temp_not_nan = temp[~temp.isnull()]
    is_in_range = ~temp_not_nan.between(-40, 70)
    sum_outside = is_in_range.sum()

    return None if sum_outside>0 else 'Its ok'

def checkVariation(df):
    temp = df.Temperature
    temp = temp.astype('float')
    prec = df.Precipitation
    prec = prec.astype('float')

    #fill nan
    temp = temp.fillna(method='backfill')
    prec = prec.fillna(method='backfill')

    #compute variations
    temp_diff = temp.diff()
    prec_diff = prec.diff()

    #check if variations are within the defined range
    sum_diff_temp = (abs(temp_diff) > 50).sum()
    sum_diff_prec = (abs(prec_diff) > 500).sum()

    return None if (sum_diff_temp>0 or sum_diff_prec>0) else 'Its ok'


