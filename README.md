# Mail-Ablage

Eine geplante Windows-Anwendung, die ausgewählte Outlook-E-Mails
und ihre Anhänge in gewöhnlichen Ordnern ablegt.

## Problem

Bisher werden E-Mails aus Outlook auf den Desktop gezogen.
Um Nachricht und Anhänge einzeln zugänglich zu machen, müssen
die Inhalte anschließend von Hand gespeichert werden.

Die Anwendung soll diese manuelle Aufbereitung übernehmen.

## Geplanter Ablauf

1. Eine oder mehrere E-Mails aus Outlook ins Fenster ziehen.
2. Optional für jede E-Mail einen eigenen Namen eingeben.
3. Auf „E-Mails speichern“ klicken.
4. Das Ergebnis für jede E-Mail im Fenster sehen.

## Ablage

Ziel ist der Ordner „Mail-Ablage“ auf dem Desktop.

Jede E-Mail bekommt einen Unterordner mit ihrem E-Mail-Datum
und einer Bezeichnung. Verwendet wird der eigene Name,
ansonsten der Betreff, ansonsten die Absenderadresse.

Gespeichert werden:

- Die Nachricht als HTML mit Absender, Empfänger, Datum und Betreff.
- Die unveränderte Original-E-Mail.
- Alle Dateianhänge im Unterordner „Anhänge“.

Vorhandene Dateien werden nicht überschrieben.
Bei gleichen Ordnernamen werden Zusätze wie „(2)“ angehängt.
Fehler werden pro E-Mail angezeigt.

## Aktueller Stand

Anforderungen und grundlegender Ablauf sind festgelegt.
Die Anwendung ist noch nicht implementiert.

Der erste technische Versuch prüft die direkte Übergabe
einer E-Mail aus Outlook unter Windows an das Programm.
