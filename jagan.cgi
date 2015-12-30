#!/usr/bin/perl
use POSIX qw(strftime);
use warnings;
use strict;
use XML::Writer;
use XML::Writer::String;
use CGI qw(:standard);
use CGI;
use Switch;
use DBI;

my $q = CGI->new;
my $section = $q->param('section');
our $user_name = $q->param('user');
my $result;
my $db = DBI->connect('DBI:mysql:billing;host=127.0.0.1', 'root','jagan') || die "Could not connect to database";
my $sql = "select * from sip_users where user=$user_name";
my $sth_trace = $db->prepare($sql);
$sth_trace->execute();
if ( $section eq 'directory' )  {
my $s = XML::Writer::String->new();
my $writer = new XML::Writer(OUTPUT => $s, DATA_MODE => 1, DATA_INDENT => 1);
while($result = $sth_trace->fetchrow_hashref()){
		print header('text/xml');
		$writer->xmlDecl('UTF-8', 'no');
		$writer->startTag('document', type=>'freeswitch/xml');
		$writer->startTag('section',name=>'directory');
		$writer->startTag('domain',name=>$result->{Domain});
		$writer->startTag('groups');
		$writer->startTag('group',name=>'public');
		$writer->startTag('users');
		$writer->startTag('user',id=>$result->{user});
		$writer->startTag('params');
		$writer->emptyTag('param',name=>'password',value=>$result->{pass});
		$writer->endTag('params');
		$writer->startTag('variables');
		$writer->emptyTag('variable',name=>'user_context',value=>'public');
		$writer->emptyTag('variable',name=>'nibble_account',value=>$result->{account_code});
        $writer->endTag('variables');
		$writer->endTag('user');
		$writer->endTag('users');
		$writer->endTag('group');
		$writer->endTag('groups');
		$writer->endTag('domain');
		$writer->endTag('section');
		$writer->endTag('document');
		$writer->end();
		print $s->value();
	}

} elsif ( $section eq 'dialplan' ) {
    my $s = XML::Writer::String->new();
	my $writer = new XML::Writer( OUTPUT => $s, DATA_MODE => 1, DATA_INDENT => 1);
	print header('text/xml');
	$writer->xmlDecl('UTF-8', 'no');
	$writer->startTag('document', type=>'freeswitch/xml');
	$writer->startTag('section',name=>'dialplan',description=>'RE DialPlan For FreeSwitch');
	$writer->startTag('context',name=>'public');
	$writer->startTag('extension',name=>'test');
	$writer->startTag('condition',field=>'destination_number',expression=>'^(\d+)$');
	$writer->emptyTag('action',application=>'set',data=>'dialed_extension=$1');
	
### ALL VARIABLES TO EXPORT #######	
my $user_name = $q->param('Caller-Username');
my $call_id_number = $q->param('Caller-Caller-ID-Number');
my $dest_number = $q->param('Caller-Destination-Number');
my $uuid = $q->param('Unique-ID');
my $context = $q->param('Caller-Context');
my $sip_authorized = $q->param('variable_sip_authorized');
my $caller_id_number = $q->param('variable_effective_caller_id_number');
my $session_id = $q->param('variable_session_id');
my $sip_from_user = $q->param('variable_sip_from_user');
my $sip_received_ip = $q->param('variable_sip_received_ip');
my $sip_acl_authed_by = $q->param('variable_sip_acl_authed_by');
my $sip_network_ip  =$q->param('variable_sip_network_ip');
my $auth_acl = $q->param('auth_acl');
my $sip_user_agent = $q->param('variable_sip_user_agent');
my $vmd = $q->param('vmd');
###########################EXPORT ALL DATA INTO CLI#########
#my( $name, $value );
#foreach $name ($q->param) 
# {
#foreach $value ( $q->param( $name ) ) {
#       $writer->emptyTag('action',application=>'export',data=>$value);
#    }
#}
###########################
my $result1;
my $db = DBI->connect('DBI:mysql:billing;host=127.0.0.1', 'root','jagan') || die "Could not connect to database";
my $sql = "select * from accounts where id=$user_name";
my $sth_trace = $db->prepare($sql);
$sth_trace->execute();
$result1 = $sth_trace->fetchrow_hashref();
my $result2;
my $sql1 = "select *  from dialplan where instr($dest_number,prefix)=1 and pricelist_id=$result1->{pricelist_id} order by id desc limit 1";
$sth_trace = $db->prepare($sql1);
$sth_trace->execute();
$result2 = $sth_trace->fetchrow_hashref();   
my $bal = $result1->{cash} ;
###ROUTE_COUNT###################
my $count_sth = $db->prepare("select count(*)  from dialplan where instr($dest_number,prefix)=1 and pricelist_id=1 order by id desc limit 1;")
                or die "Prepare Count Error: $DBI::errstr\n";

$count_sth->execute()
           or die "Execute Count Error: $DBI::errstr\n";

my $route_count =$count_sth->fetchrow;



print $route_count;

print "\n\n";

$count_sth->finish;
$db->disconnect;

#################################
$writer->emptyTag('action',application=>'log',data=>$route_count);
$writer->emptyTag('action',application=>'log',data=>$sql1);
##BALANCE CHECKING ##
if ($bal >= 0.3 && $route_count > 0){
 $writer->emptyTag('action',application=>'export',data=>"user_name=".$user_name."");
 $writer->emptyTag('action',application=>'export',data=>"dest_number=".$dest_number."");
 $writer->emptyTag('action',application=>'export',data=>"call_id_number=".$call_id_number."");
 $writer->emptyTag('action',application=>'export',data=>"uuid=".$uuid."");
 $writer->emptyTag('action',application=>'export',data=>"context=".$context."");
 $writer->emptyTag('action',application=>'export',data=>"sip_authorized=".$sip_authorized."");
 $writer->emptyTag('action',application=>'export',data=>"session_id=".$session_id."");
 $writer->emptyTag('action',application=>'export',data=>"sip_from_user=".$sip_from_user."");
 $writer->emptyTag('action',application=>'export',data=>"sip_received_ip=".$sip_received_ip."");
 $writer->emptyTag('action',application=>'export',data=>"sip_acl_authed_by=".$sip_acl_authed_by."");
 $writer->emptyTag('action',application=>'export',data=>"customer_ip=".$sip_network_ip."");
 $writer->emptyTag('action',application=>'export',data=>"auth_acl=".$auth_acl."");
 $writer->emptyTag('action',application=>'export',data=>"sip_user_agent=".$sip_user_agent."");
 $writer->emptyTag('action',application=>'export',data=>"price_lits=".$result1->{pricelist_id}."");
 $writer->emptyTag('action',application=>'export',data=>"nibble_rate=".$result2->{price_sell}."");
 $writer->emptyTag('action',application=>'export',data=>"gateway=".$result2->{provider}."");
 $writer->emptyTag('action',application=>'export',data=>"incriment=".$result2->{incriment}."");
 $writer->emptyTag('action',application=>'export',data=>"prefix=".$result2->{prefix}."");
 $writer->emptyTag('action',application=>'bridge',data=>'sofia/gateway/MY80/$1');
 $writer->endTag('condition');
 $writer->endTag('extension');
 $writer->endTag('context');
 $writer->endTag('section');
 $writer->endTag('document');
 $writer->end();
	print $s->value();
}	
	
else {
##HANGUP WITH CINGESTION NO BALANCE###
    $writer->emptyTag('action',application=>'hangup',data=>'SWITCH_CONGESTION');
	$writer->endTag('condition');
	$writer->endTag('extension');
	$writer->endTag('context');
	$writer->endTag('section');
	$writer->endTag('document');
	$writer->end();
	print $s->value();

}

} 
 else {
	my $result;
	my $s = XML::Writer::String->new();
	my $writer = new XML::Writer( OUTPUT => $s, DATA_MODE => 1, DATA_INDENT => 1);
	print header('text/xml');
	$writer->xmlDecl('UTF-8', 'no');
	$writer->startTag('document', type=>'freeswitch/xml');
	$writer->startTag('section',name=>'result');
	$writer->emptyTag('result',status=>'not fount');
	$writer->endTag('section');
	$writer->endTag('document');
}

1;


