uses FormsABC;
 
 var 
  r := new IntegerField('r:');
  r1 := new FlowBreak;
  m := new IntegerField('m:');
  m1 := new FlowBreak;
  f1 := new FlowBreak(20);
  s1 := new Space(10);
  b := new Button('Вычислить');
  tb: TextBox;

procedure MyClick;
begin
  tb.Undo();
  var res:= r.Value*m.Value;
  tb.AddLine(res.ToString);
end;
 
begin
  b.Click += MyClick;
  MainForm.Title := 'Задача';
  MainForm.SetSize(500,350);
  MainForm.CenterOnScreen;
  
  mainPanel.Dock := DockStyle.Top;
  mainPanel.Width := 150;
  ParentControl := MainForm;
  tb := new TextBox;
  tb.Dock := DockStyle.Fill;  
end.
