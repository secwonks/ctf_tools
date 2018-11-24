#!/bin/bash
#Scripted telnet input for phishing assessment
read -p "Enter URL: " link

# create message
function mail_input {
echo "ehlo mail.syn-pi.org"
echo "MAIL FROM: julie@syn-pi.org"
echo "RCPT TO: freddy@syn-pi.org"
echo "DATA"
echo "From: julie@syn-pi.org"
echo "To: freddy@syn-pi.org"
echo "Subject: Account Activation"
echo "$link"
echo "."
echo "quit"
}

mail_input | telnet mail.syn-pi.org 25
