; installer.iss

[Setup]
AppName=Simple .TXT Duplicate Cleaner
AppVersion=1.0
DefaultDirName={pf}\Simple .TXT Duplicate Cleaner
DefaultGroupName=Simple .TXT Duplicate Cleaner
OutputBaseFilename=SimpleTXTDuplicateCleanerSetup
Compression=lzma
SolidCompression=yes
SetupIconFile=icon.ico
UninstallDisplayIcon={app}\Simple .TXT Duplicate Cleaner.exe
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked

[Files]
Source: "Simple .TXT Duplicate Cleaner.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Simple .TXT Duplicate Cleaner"; Filename: "{app}\Simple .TXT Duplicate Cleaner.exe"
Name: "{commondesktop}\Simple .TXT Duplicate Cleaner"; Filename: "{app}\Simple .TXT Duplicate Cleaner.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\Simple .TXT Duplicate Cleaner.exe"; Description: "Launch Simple .TXT Duplicate Cleaner"; Flags: nowait postinstall skipifsilent
