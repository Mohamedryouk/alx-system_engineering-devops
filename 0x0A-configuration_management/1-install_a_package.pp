#1-insall_a_package.pp
package{      'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}