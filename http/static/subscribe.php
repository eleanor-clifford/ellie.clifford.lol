<?php
$email = $_POST["email"];
$error = "";
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
	$error.="Invalid email address. If you're trying to hack me I'll be mad 😠";
} else {
	// fix ' to outwit the hackers
	$email = str_replace("'", "'\"'\"'", $email);
	$output = null;
	$retval = null;
	// hardcode paths and stuff for extra security
	//exec("echo '".$email."' | /usr/bin/ssh shell.srcf.net /usr/local/bin/srcf-mailman-add tc565-blog >> /home/tc565/logs/web-mailman 2>&1", $output, $retval);
	//if ($retval != 0)
		//$error = "Failed to add email address. Please email me so I can fix it :) Exit code: ".$retval;
	//
	// logging
	//$logfile = fopen("/home/tc565/logs/blog_subscribe_POST", "a");
	//$fwrite(
}
?>
<html lang="en">
  <head>
    <title>Email subscription</title>
    <link rel="icon" type="image/jpeg" href="/avatar_48.jpg"/>
    <meta charSet="utf-8"/>
    <meta content="width=device-width, initial-scale=1" name="viewport"/>
    <link rel="stylesheet" type="text/css" href="/main.css?v4"/>
  </head>
  <body>
    <div class="purple">
      <div class="topbar">
        <nav>
          <a class="topbar-title" href="/">
            <img src="/avatar_transparent_256.png"/>
          </a>
          <a class="topbar-toggle" href="https://eleanor.clifford.lol">
            <img src="/toggle.svg"/>
            <p>Toggle silliness</p>
          </a>
          <ul>
            <li>
              <a href="/about/" class="topbar-button left">About</a>
            </li>
            <li>
              <a href="/music/" class="topbar-button middle">Music</a>
            </li>
            <li>
              <a href="/blog/" class="topbar-button right">Blog</a>
            </li>
          </ul>
        </nav>
      </div>
      <div class="single">
        <div class="wrap"><div class="page">
          <p/>
          <p/>
<?php
//if (strlen($error) == 0) {
if (false) {
?>
    <span>Successfully subscribed <?php echo $email?></span>
    <p/>
    <p>
      Thanks for the support! You should receive email confirmation. To
      unsubscribe, email tc565-blog-request@srcf.net with subject line
      "unsubscribe"
    </p>
<?php
} else {
	echo '<span style="color: #ff5555; font-weight: bold;">Down for maintenance due to spam. For now, please subscribe via <a href="gemini://ellie.clifford.lol/blog/">gemini://ellie.clifford.lol/blog/</a> or contact me through an alternate channel.</span>';
	http_response_code(503);
}
?>
        </div></div>
      </div>
      <div class="footer">
        <table class="noborder" style="border: 0px solid; width: 100%"><tr>
          <td><a href="https://www.srcf.net" class="nounderline">
            <img style="min-height: 48pt; padding-right:10pt"
                 src="/srcf.svg" alt="The logo of the SRCF"></img>
          </a></td>
          <td style="text-align: center"><i>
            This site is hosted by the Student Run Computing Facility, and
            uses a Dracula theme
          </i></td>
          <td><a href="https://draculatheme.com" class="nounderline">
            <img style="min-height: 48pt; padding-left:10pt"
                 src="/dracula.svg" alt="The logo of the Dracula theme">
            </img>
          </a></td>
        </tr></table>
      </div>
    </div>
  </body>
</html>
