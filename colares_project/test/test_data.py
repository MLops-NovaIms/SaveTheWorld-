from .. import downloadData, cleanDownloadedData
import pytest



def test_DownloadResult():
    assert downloadData()

@pytest.fixture
def df():
    return cleanDownloadedData(downloadData())



def test_checkNumFormat(df):

    prec = df.Precipitation
    temp = df.Temperature

    try:
        check_prec = prec.astype('float')
        check_temp = temp.astype('float')
    except:
        check_prec = None
        check_temp = None
    
    assert (check_prec is not None and check_temp is not None)
    #return None if (check_prec is None or check_temp is None) else 'Its ok'

def test_checkPrecRange(df):
    prec = df.Precipitation
    prec = prec.astype('float')
    prec_not_nan = prec[~prec.isnull()]
    is_in_range = ~prec_not_nan.between(0, 1000)
    sum_outside = is_in_range.sum()

    assert sum_outside==0
    #return None if sum_outside>0 else 'Its ok'

def test_checkPrecRange(df):
    temp = df.Temperature
    temp = temp.astype('float')
    temp_not_nan = temp[~temp.isnull()]
    is_in_range = ~temp_not_nan.between(-40, 70)
    sum_outside = is_in_range.sum()

    assert sum_outside==0
    #return None if sum_outside>0 else 'Its ok'

def test_checkVariation(df):
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

    assert (sum_diff_temp==0 and sum_diff_prec==0)
    #return None if (sum_diff_temp>0 or sum_diff_prec>0) else 'Its ok'


