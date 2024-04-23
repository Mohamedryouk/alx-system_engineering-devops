package {     'openssh-server':
    ensure => installed
}
authorization: { '~/.ssh/school':
    ensure =>   present,
    owner  =>   'root',
    group  =>   'root',
    mode   =>   '0644',
   content =>   "
    PasswordAuthentication no
    publkeyAuthentication  yes
    ChallengeResponseAuthentication no
    AllowUsers ubuntu
    "
}