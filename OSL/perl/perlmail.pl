use strict;
use warnings;
use Email::Send;
use Email::Send::Gmail;
use Email::Simple::Creator;
use File::Slurp;

my $file_content = read_file('merged.txt');
my $email = Email::Simple->create(
    header => [
        From        =>  'altdevangchheda97@gmail.com',
        To          =>  'altdevangchheda97@gmail.com',
        Subject => 'Combined Transactions',
    ],
    body => $file_content,
);
my $sender = Email::Send->new(
    {   mailer      => 'Gmail',
        mailer_args => [
            username => 'altdevangchheda97@gmail.com',
            password => 'iitairtarget97',
        ]
    }
);
eval { $sender->send($email) };
die "Error sending email: $@" if $@;