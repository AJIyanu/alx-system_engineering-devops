# me i wanna install flask on my pc with pip

package { 'flask':
  ensure   => '2.1.0',
  provider => pip3,
}
