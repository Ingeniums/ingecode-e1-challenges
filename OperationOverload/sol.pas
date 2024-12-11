program OperationOverlord;

const
  MaxRows = 10;
  MaxCols = 10;
  MaxQueue = 1000;

type
  TNode = record
    x, y, steps: Integer;
  end;

  TQueue = record
    data: array[1..MaxQueue] of TNode;
    front, rear: Integer;
  end;

var
  Grid: array[0..MaxRows - 1, 0..MaxCols - 1] of Integer;
  Visited: array[0..MaxRows - 1, 0..MaxCols - 1] of Boolean;
  Directions: array[1..4, 1..2] of Integer;
  Results: String;

procedure Enqueue(var Q: TQueue; x, y, steps: Integer);
begin
  Inc(Q.rear);
  Q.data[Q.rear].x := x;
  Q.data[Q.rear].y := y;
  Q.data[Q.rear].steps := steps;
end;

function Dequeue(var Q: TQueue): TNode;
begin
  Dequeue := Q.data[Q.front];
  Inc(Q.front);
end;

function IsEmpty(var Q: TQueue): Boolean;
begin
  IsEmpty := Q.front > Q.rear;
end;

function BFS(rows, cols, startX, startY, endX, endY: Integer): Integer;
var
  Q: TQueue;
  i, nx, ny: Integer;
  Current: TNode;
begin
  // Reset visited array
  FillChar(Visited, SizeOf(Visited), False);
  Q.front := 1;
  Q.rear := 0;

  // Initialize BFS
  Enqueue(Q, startX, startY, 0);
  Visited[startX][startY] := True;

  while not IsEmpty(Q) do
  begin
    Current := Dequeue(Q);

    if (Current.x = endX) and (Current.y = endY) then
      Exit(Current.steps);

    for i := 1 to 4 do
    begin
      nx := Current.x + Directions[i, 1];
      ny := Current.y + Directions[i, 2];

      if (nx >= 0) and (ny >= 0) and (nx < rows) and (ny < cols) and
         (Grid[nx, ny] = 0) and not Visited[nx, ny] then
      begin
        Visited[nx, ny] := True;
        Enqueue(Q, nx, ny, Current.steps + 1);
      end;
    end;
  end;

  Exit(-1); // No path found
end;

var
  InputFile: Text;
  rows, cols, startX, startY, endX, endY, i, j, result: Integer;
  tempStr: String;

begin
  Directions[1, 1] := 0; Directions[1, 2] := 1;  // Right
  Directions[2, 1] := 1; Directions[2, 2] := 0;  // Down
  Directions[3, 1] := 0; Directions[3, 2] := -1; // Left
  Directions[4, 1] := -1; Directions[4, 2] := 0; // Up

  Assign(InputFile, 'test_cases.txt');
  Reset(InputFile);
  Results := '';
  
  while not EOF(InputFile) do
  begin
    ReadLn(InputFile, rows, cols);
    for i := 0 to rows - 1 do
    begin
      for j := 0 to cols - 1 do
      begin
        Read(InputFile, Grid[i, j]);
      end;
      ReadLn(InputFile);
    end;
    ReadLn(InputFile, startX, startY);
    ReadLn(InputFile, endX, endY);

    result := BFS(rows, cols, startX, startY, endX, endY);

    Str(result, tempStr); //str hadi t3 sh3ar 9adr tzid 0 at the end be carful
    Results := Results + tempStr;
  end;

  Close(InputFile);

  WriteLn('Flag: ', Results);
end.
