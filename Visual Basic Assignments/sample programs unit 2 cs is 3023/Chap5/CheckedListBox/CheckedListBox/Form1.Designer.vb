<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.clbCities = New System.Windows.Forms.CheckedListBox()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.lstChecked = New System.Windows.Forms.ListBox()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.Button1 = New System.Windows.Forms.Button()
        Me.SuspendLayout()
        '
        'clbCities
        '
        Me.clbCities.CheckOnClick = True
        Me.clbCities.FormattingEnabled = True
        Me.clbCities.Items.AddRange(New Object() {"Atlanta", "Chicago", "Los Angeles", "New York", "San Francisco", "Raleigh"})
        Me.clbCities.Location = New System.Drawing.Point(21, 41)
        Me.clbCities.Margin = New System.Windows.Forms.Padding(4, 4, 4, 4)
        Me.clbCities.Name = "clbCities"
        Me.clbCities.Size = New System.Drawing.Size(159, 130)
        Me.clbCities.TabIndex = 0
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(18, 20)
        Me.Label1.Margin = New System.Windows.Forms.Padding(4, 0, 4, 0)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(168, 17)
        Me.Label1.TabIndex = 1
        Me.Label1.Text = "Select one or more cities."
        '
        'lstChecked
        '
        Me.lstChecked.FormattingEnabled = True
        Me.lstChecked.ItemHeight = 16
        Me.lstChecked.Location = New System.Drawing.Point(205, 41)
        Me.lstChecked.Margin = New System.Windows.Forms.Padding(4, 4, 4, 4)
        Me.lstChecked.Name = "lstChecked"
        Me.lstChecked.Size = New System.Drawing.Size(159, 132)
        Me.lstChecked.TabIndex = 2
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(202, 20)
        Me.Label2.Margin = New System.Windows.Forms.Padding(4, 0, 4, 0)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(94, 17)
        Me.Label2.TabIndex = 3
        Me.Label2.Text = "You checked:"
        '
        'Button1
        '
        Me.Button1.Location = New System.Drawing.Point(154, 192)
        Me.Button1.Margin = New System.Windows.Forms.Padding(4, 4, 4, 4)
        Me.Button1.Name = "Button1"
        Me.Button1.Size = New System.Drawing.Size(100, 28)
        Me.Button1.TabIndex = 4
        Me.Button1.Text = "OK"
        Me.Button1.UseVisualStyleBackColor = True
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(8.0!, 16.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(387, 237)
        Me.Controls.Add(Me.Button1)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.lstChecked)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.clbCities)
        Me.Font = New System.Drawing.Font("Microsoft Sans Serif", 10.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Margin = New System.Windows.Forms.Padding(4, 4, 4, 4)
        Me.Name = "Form1"
        Me.Text = "Checked List Box"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents clbCities As Windows.Forms.CheckedListBox
    Friend WithEvents Label1 As Label
    Friend WithEvents lstChecked As ListBox
    Friend WithEvents Label2 As Label
    Friend WithEvents Button1 As Button
End Class
