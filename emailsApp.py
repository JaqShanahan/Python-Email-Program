from email import message
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from keyboard import send

# your email goes here
sender_email = "youremail@gmail.com"

print("""
██╗  ██╗███████╗██████╗ ███╗   ███╗███████╗███████╗    ███████╗███╗   ███╗ █████╗ ██╗██╗     ███████╗██████╗ 
██║  ██║██╔════╝██╔══██╗████╗ ████║██╔════╝██╔════╝    ██╔════╝████╗ ████║██╔══██╗██║██║     ██╔════╝██╔══██╗
███████║█████╗  ██████╔╝██╔████╔██║█████╗  ███████╗    █████╗  ██╔████╔██║███████║██║██║     █████╗  ██████╔╝
██╔══██║██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══╝  ╚════██║    ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     ██╔══╝  ██╔══██╗
██║  ██║███████╗██║  ██║██║ ╚═╝ ██║███████╗███████║    ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝    ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
Shanahan Information and Technology Inc. 2022
Send emails with ease. 
                                                                                                             """)

with open("text_files/email_answers.txt", "r") as ug:
        email_answers = ug.read().split(',')


loop = True
while loop == True:
  #sending to the email address you want to send to
  receiver_email = input("Who would you like to send an email to? ")
  # your email password
  password = "yourpassword"

  message = MIMEMultipart("alternative")
  message["Subject"] = input("What is the subject of the email? ")
  message["From"] = sender_email
  message["To"] = receiver_email

  title_text = input("What would you like the title to be, you could make it the same as the header? ")
  body_text = input("""What would you like the email to say? 
  For a new line type <br> and when you are finished press enter.
  """)

  html = """
  <!DOCTYPE html>
  <html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">

  <head>
    <title></title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
    <style>
      * {
        box-sizing: border-box;
      }

      body {
        margin: 0;
        padding: 0;
      }

      a[x-apple-data-detectors] {
        color: inherit !important;
        text-decoration: inherit !important;
      }

      #MessageViewBody a {
        color: inherit;
        text-decoration: none;
      }

      p {
        line-height: inherit
      }

      .desktop_hide,
      .desktop_hide table {
        mso-hide: all;
        display: none;
        max-height: 0px;
        overflow: hidden;
      }

      @media (max-width:520px) {

        .desktop_hide table.icons-inner,
        .social_block.desktop_hide .social-table {
          display: inline-block !important;
        }

        .icons-inner {
          text-align: center;
        }

        .icons-inner td {
          margin: 0 auto;
        }

        .image_block img.big,
        .row-content {
          width: 100% !important;
        }

        .mobile_hide {
          display: none;
        }

        .stack .column {
          width: 100%;
          display: block;
        }

        .mobile_hide {
          min-height: 0;
          max-height: 0;
          max-width: 0;
          overflow: hidden;
          font-size: 0px;
        }

        .desktop_hide,
        .desktop_hide table {
          display: table !important;
          max-height: none !important;
        }
      }
    </style>
  </head>

  <body style="background-color: #FFFFFF; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
    <table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #FFFFFF;">
      <tbody>
        <tr>
          <td>
            <table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
              <tbody>
                <tr>
                  <td>
                    <table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 500px;" width="500">
                      <tbody>
                        <tr>
                          <td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
                            <table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                              <tr>
                                <td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
                                  <div class="alignment" align="center" style="line-height:10px"><img class="big" src="https://d15k2d11r6t6rl.cloudfront.net/public/users/Integrators/BeeProAgency/877944_862119/editor_images/63e0b0b2-42c0-436a-94f3-35d72c9993cb.png" style="display: block; height: auto; border: 0; width: 500px; max-width: 100%;" width="500"></div>
                                </td>
                              </tr>
                            </table>
                            <table class="html_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                              <tr>
                                <td class="pad">
                                  <div style="font-family:Arial, Helvetica Neue, Helvetica, sans-serif;text-align:center;" align="center"><table border="0" cellpadding="0" cellspacing="10px" style="padding:0px 0px 10px 0px">
    <tr>
      <td>
        <h2 style="text-align:left">""" + f"{title_text}" + """</h2>
        <p style="text-align:left">
          """ + f"{body_text}" + """<br /><br />Sincerely,<br />Jaq
        </p>
      </td>
    </tr>
  </table></div>
                                </td>
                              </tr>
                            </table>
                            <table class="html_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                              <tr>
                                <td class="pad">
                                  <div style="font-family:Arial, Helvetica Neue, Helvetica, sans-serif;text-align:center;" align="center"><table width="100%" style="margin-top:25px">
    <tr>
      <td align="center" style="padding:30px 30px">

        <h3>Jaq Shanahan</h3> 
        <p style="margin-top:-10px">
          +61413363945<br />
          Adelaide, Australia

        </p>

        <a href="mailto:""" + f"{sender_email}" + """?subject = Feedback&amp;body = Message">
          Send Me a Message
        </a>
      </td>
    </tr>
  </table></div>
                                </td>
                              </tr>
                            </table>
                            <table class="social_block block-4" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                              <tr>
                                <td class="pad">
                                  <div class="alignment" style="text-align:center;">
                                    <table class="social-table" width="126px" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block;">
                                      <tr>
                                        <td style="padding:0 5px 0 5px;"><a href="https://www.facebook.com/Jaq.Lloyd" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-dark-gray/facebook@2x.png" width="32" height="32" alt="Facebook" title="facebook" style="display: block; height: auto; border: 0;"></a></td>
                                        <td style="padding:0 5px 0 5px;"><a href="https://www.linkedin.com/in/jaq-shanahan-a327ba21a/" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-dark-gray/linkedin@2x.png" width="32" height="32" alt="Linkedin" title="linkedin" style="display: block; height: auto; border: 0;"></a></td>
                                        <td style="padding:0 5px 0 5px;"><a href="https://www.instagram.com/jaqshanahan/" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-dark-gray/instagram@2x.png" width="32" height="32" alt="Instagram" title="instagram" style="display: block; height: auto; border: 0;"></a></td>
                                      </tr>
                                    </table>
                                  </div>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
      </tbody>
    </table><!-- End -->
  </body>

  </html>
  """

  part2 = MIMEText(html, "html")

  message.attach(part2)


  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
      sender_email, receiver_email, message.as_string()
      )

  userChoice = input("Would you like to send another email? ")
  if userChoice.lower() in email_answers:
    loop = False

