#1-insall_a_package.pp
package{      'flask':
  ensure   => installed,
  provider => 'pip3',
}