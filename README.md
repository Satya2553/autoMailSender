<!DOCTYPE html>
<html>
<body>
  <h1>Automated Email Sender (Python, MIME, SMTP)</h1>
  
  <h2>Prerequisites</h2>
  <p>To run this script, you need to have the following:</p>
  <ul>
    <li>Python 3.x installed on your system</li>
    <li>The <code>smtplib</code> module, which can be installed via <code>pip</code>:</li>
  </ul>
  <pre><code>pip install secure-smtplib</code></pre>
  
  <h2>Configuration</h2>
  <ol>
    <li>Open the <code>send_email.py</code> file in a text editor.</li>
    <li>Replace the empty strings (<code>""</code>) in the following lines with your own email credentials:</li>
  </ol>
  <pre><code>
sender_email = ""  // enter your email address here
receiver_email = ""  // enter the recipient's email address here
password = ""  // enter your email password here
  </code></pre>
  
  <h2>Usage</h2>
  <ol>
    <li>Open a terminal or command prompt.</li>
    <li>Navigate to the directory where the <code>send_email.py</code> file is located.</li>
    <li>Run the script using the following command:</li>
  </ol>
  <pre><code>python send_email.py</code></pre>
  <p>The script will prompt you for necessary inputs, such as the email subject and body.</p>
  <p>Once you provide the required information, the script will send the email using the provided SMTP server.</p>
</body>
</html>
