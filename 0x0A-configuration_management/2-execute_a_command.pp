# usimg the ezecute command. pkill

exec { 'pkill':
      path     => '/bin/',
      commandm => 'pkill killmenow'
      provider => shell,
      return   => [0, 1],
}
