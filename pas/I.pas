uses FormsABC;
 
 var 
  t1 := new IntegerField('t1:');
  t11 := new FlowBreak;
  t2 := new IntegerField('t2:');
  t22 := new FlowBreak;
  q1 := new IntegerField('q1:');
  q11 := new FlowBreak;
  q2 := new IntegerField('q2:');
  q22 := new FlowBreak;
  f1 := new FlowBreak(20);
  s1 := new Space(10);
  b := new Button('Вычислить');
  tb: TextBox;

procedure MyClick;
begin
  tb.Undo();
  var res:= (q2.Value-q1.Value)/(t2.Value-t1.Value);
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
