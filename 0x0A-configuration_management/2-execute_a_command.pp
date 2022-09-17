# usimg the ezecute command. pkill

exec { 'pkill':
	command => ['/bin/pkill', 'killmenow']
}
