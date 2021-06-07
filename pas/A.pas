uses FormsABC;
 
 var 
  R := new IntegerField('R:');
  c1 := new FlowBreak;
  t1 := new IntegerField('t1:');
  t11 := new FlowBreak;
  t2 := new IntegerField('t2:');
  t22 := new FlowBreak;
  m := new IntegerField('m:');
  m2 := new FlowBreak;
  M1 := new IntegerField('M:');
  m3 := new FlowBreak;
  f1 := new FlowBreak(20);
  s1 := new Space(10);
  b := new Button('Вычислить');
  tb: TextBox;

procedure MyClick;
begin
  tb.Undo();
  var res:= (-3/2)*(m.Value/M.Value)*(R.Value*(t2.Value-t1.Value));
  tb.AddLine(res.ToString);
end;
 
begin
  b.Click += MyClick;
  MainForm.Title := 'Задача';
  MainForm.SetSize(500,350);
  MainForm.CenterOnScreen;
  
  mainPanel.Dock := DockStyle.Top;
  mainPanel.Width := 180;
  ParentControl := MainForm;
  tb := new TextBox;
  tb.Dock := DockStyle.Fill;  
end.
