uses FormsABC;
 
 var 
  c := new IntegerField('C:');
  c1 := new FlowBreak;
  u := new IntegerField('U:');
  u11 := new FlowBreak;
  f1 := new FlowBreak(20);
  s1 := new Space(10);
  b := new Button('Вычислить');
  tb: TextBox;

procedure MyClick;
begin
  tb.Undo();
  var res:= (c.Value*(u).Value*u.Value)/2;
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
