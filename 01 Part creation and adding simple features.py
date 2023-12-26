# pip install pywin32
from win32com.client import Dispatch, GetActiveObject, gencache

# Get Inventor Application
try:
    invApp = GetActiveObject('Inventor.Application')
except:
    invApp = Dispatch('Inventor.Application')
    invApp.Visible = True

mod = gencache.EnsureModule('{D98A091D-3A0F-4C3E-B36E-61F62068D488}', 0, 1, 0)
constants = mod.constants
invApp = mod.Application(invApp)
invApp.SilentOperation = True

# Create a new part
part_template = "C:/Users/Public/Documents/Autodesk/Inventor 2023/Templates/ru-RU/Standard.ipt"
invDoc = invApp.Documents.Add(constants.kPartDocumentObject, part_template, True)

# Cast this doc to a PartDocument, so we can use its structure
invPartDoc = mod.PartDocument(invDoc)
compdef = invPartDoc.ComponentDefinition

# creating a sketch
sketch = compdef.Sketches.Add(compdef.WorkPlanes.Item(3))

# add lines into a sketch
tg = invApp.TransientGeometry

# coordinates will be increased tenfold (because cm is internal Inventor API units)
first_point = tg.CreatePoint2d(0, 0)
second_point = tg.CreatePoint2d(100, 50)
sketch.SketchLines.AddAsTwoPointCenteredRectangle(first_point, second_point)
