Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim intIndex As Integer ' List box index

        ' Clear any previous selections shown in the ListBox.
        lstChecked.Items.Clear()

        ' Get the checked items.
        For intIndex = 0 To clbCities.Items.Count - 1
            If clbCities.GetItemChecked(intIndex) = True Then
                lstChecked.Items.Add(clbCities.Items(intIndex))
            End If
        Next
    End Sub
End Class
