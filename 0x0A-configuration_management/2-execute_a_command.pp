# 2-execute_a_command.pp

exec { 'kill_killmenow_process':
  command     => 'pkill -f killmenow',
  path        => ['/usr/bin', '/bin'], # Adjust the path as needed
  onlyif      => 'pgrep -f killmenow',  # Only execute if the process is running
}
