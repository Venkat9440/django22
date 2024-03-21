import csv
from django.core.mail import send_mail
from django.shortcuts import render


def send_emails(request):
    # Update the path to the CSV file
    csv_file_path = r'C:\SDP project2\static\Emaillist.csv'

    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_email = row['EMAIL']
            subject = 'Hello friends'  # Corrected the spelling of 'friends'
            message_body = 'Hey, Welcome to PFSD Class, Hope you have a great time with Python'  # Corrected the spelling of 'you'
            send_mail(
                subject,
                message_body,
                '2200032689cseh@gmail.com',  # Update with your sender email
                [recipient_email],
                fail_silently=True,  # Set to True during production, False during development if you want to see errors
            )
            print(f'Sent email to {recipient_email}')

    return render(request, 'Emails_sent_successfully.html')