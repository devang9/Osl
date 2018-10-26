use strict;
use warnings;

my @files = ('a.txt','t1.txt','t2.txt');
my @fh;

#create an array of open filehandles.
@fh = map { open my $f, $_ or die "Cant open $_:$!"; $f } @files;

open my $out_file, ">merged.txt" or die "can't open out_file: $!";

my $output;
do
{
    $output = '';

    foreach (@fh)
    {
        my $line = <$_>;
        if (defined $line)
        {
            #Special case: might not be a newline at the end of the file
            #add a newline if none is found.
            $line .= "\n" if ($line !~ /\n$/);
            $output .= $line;
        }
    }

    print {$out_file} $output;
}
while ($output ne '');
my $t = `perl perlmail.pl`;
print $t;