program SolChallenge;

uses SysUtils;

function CountOccurrences(const s: string; const seq: string): Integer;
var
  i, count, len: Integer;
begin
  count := 0;
  len := Length(seq);
  for i := 1 to Length(s) - len + 1 do
    if Copy(s, i, len) = seq then
      Inc(count);
  CountOccurrences := count;
end;

procedure SolveChallenge(filename: string);
var
  fileText: TextFile;
  line, randomString: string;
  count: Integer;
  finalBinary: string;
begin
  Assign(fileText, filename);
  Reset(fileText);
  
  finalBinary := '';

  while not Eof(fileText) do
  begin
    ReadLn(fileText, line);
    if Pos('Random String:', line) = 1 then
    begin
      randomString := Trim(Copy(line, Pos(':', line) + 1, Length(line)));
      count := CountOccurrences(randomString, ':-|');
      if count mod 2 = 0 then
        finalBinary := finalBinary + '0'
      else
        finalBinary := finalBinary + '1';
    end;
  end;

  Close(fileText);
  WriteLn('Final Binary Code: ', finalBinary);
end;

begin
  SolveChallenge('test_cases.txt');
end.
