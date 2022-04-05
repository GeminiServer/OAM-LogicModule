Write-Host Suche COM-Port fuer SAMD...
$portList = get-pnpdevice -class Ports -PresentOnly
if ($portList) {
    foreach($device in $portList) {
        $isCom = $device.Name -match "COM(\d{1,3})"
        if($isCom)
        {
            Write-Host Gefunden $port
            $port = $Matches[0]
            break
        }
    }
    if($port)
    {
        Write-Host Verwende $port
        $serial = new-Object System.IO.Ports.SerialPort $port,1200,None,8,1
        $serial.Open()
        $serial.Close()
        Start-Sleep -s 1
         ~\bin\bossac --info --write --verify --reset --erase firmware.bin
    } else {
       Write-Host Kein Port gefunden!
    }
}
timeout /T 20 