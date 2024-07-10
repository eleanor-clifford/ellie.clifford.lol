recipients="$(ssh pip srcf-mailman-list ecc73-blog | sed -z 's/\n$//;s/\n/ /g')"

<$1 msmtp-dkim -- blog-test@clifford.lol

echo -n "Sent test email. "
echo "Press enter to send to: "
echo "$recipients"
echo "or ctrl-c to cancel"

read foo

<$1 msmtp-dkim -- $recipients
