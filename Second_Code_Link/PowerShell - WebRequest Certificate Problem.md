# To download it with pure Powershell we just need to skip the certificate validation, as the site does not have a valid certificate for the name it is using,

# Code: 

Invoke-WebRequest -SkipCertificateCheck -Uri "https://snirh.pt/snirh/_dadosbase/site/paraCSV/dados_csv.php?sites=920685260&pars=
1436794570,1520200094&tmin=01/10/1965&tmax=10/03/2022&formato=csv" -Outfile "dados.csv"

# For the SkipCertificateCheck flag to be available Powershell 7 is required. It can be easily downloaded from the Microsoft Store.

https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.2
https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest?view=powershell-7.2
