#!/usr/bin/env python3
import re

# Path to the leafProperties file
leaf_file = "constant/leafProperties"

# Read the entire contents of the leafProperties file
with open(leaf_file, 'r') as f:
    text = f.read()

# Extract the LADCoeffs block from the file using regex
lad_block = re.search(r'LADCoeffs\s*\{([^}]+)\}', text)
if lad_block:
    # Get the text inside the LADCoeffs block
    lad_text = lad_block.group(1)
    
    # Search for the value corresponding to 'trees'
    trees_match = re.search(r'trees\s+([\d\.]+);', lad_text)
    # Search for the value corresponding to 'pots'
    pots_match = re.search(r'pots\s+([\d\.]+);', lad_text)
    
    if trees_match and pots_match:
        LAD_trees = trees_match.group(1)
        LAD_pots = pots_match.group(1)
        
        # Write the new setFieldsDict file with the values extracted
        with open("system/setFieldsDict", 'w') as f:
            f.write("""/*--------------------------------*- C++ -*----------------------------------*\\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\\\    /   O peration     | Version:  v2312                                 |
|   \\\\  /    A nd           | Website:  www.openfoam.com                      |
|    \\\\/     M anipulation  |                                                 |
\\*---------------------------------------------------------------------------*/
FoamFile
{{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      setFieldsDict;
}}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

defaultFieldValues
(
    volScalarFieldValue LAD 0.0
);

regions
(
    cellToCell
    {{
        name trees;
        set trees;
        fieldValues
        (
            volScalarFieldValue LAD {trees}
        );
    }}

    cellToCell
    {{
        name pots;
        set pots;
        fieldValues
        (
            volScalarFieldValue LAD {pots}
        );
    }}
);

// ************************************************************************* //
""".format(trees=LAD_trees, pots=LAD_pots))
        print("✅ setFieldsDict generated successfully.")
    else:
        print("❌ Could not find the values for 'trees' or 'pots' in LADCoeffs.")
else:
    print("❌ LADCoeffs block not found in leafProperties.")
