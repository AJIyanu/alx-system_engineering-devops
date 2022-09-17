# usimg the ezecute command. pkill

exec { 'pkill':
  command => 'pkill "killmenow"',
}
