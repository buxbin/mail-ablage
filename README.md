# Mail Archive

A planned Windows application that saves selected Outlook emails
and their attachments in regular folders.

## Problem

Currently, emails are dragged from Outlook onto the desktop.
The message and attachments then have to be saved manually
to make them accessible as separate files.

The application will automate this manual process.

## Planned workflow

1. Drag one or more emails from Outlook into the window.
2. Optionally enter a custom name for each email.
3. Click "Save emails".
4. View the result for each email in the window.

## Storage

The destination is a folder named "Mail Archive" on the desktop.

Each email gets a subfolder named using its email date and a label.
The label is the custom name if provided, otherwise the subject,
or the sender's email address if the subject is empty.

Each folder contains:

- The message as HTML, including sender, recipients, date, and subject.
- The unchanged original email file received from Outlook.
- All file attachments in an "Attachments" subfolder.

Existing files are never overwritten.
If a folder name already exists, a suffix such as "(2)" is added.
Errors are reported separately for each email.

## Current status

The requirements and basic workflow have been defined.
The application has not been implemented yet.

The first technical experiment will test whether the application
can receive an email dragged directly from Outlook on Windows.
