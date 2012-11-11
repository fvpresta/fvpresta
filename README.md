fvpresta
========

Naming convention:

- Template file name: always use the normal chars, not capitalized ones and separated by _
    + Normal file: normal_file.html (serves to display with render_to_response and can include partial files, thus must alway have 'extends')
    + Partial file/ Include file: _partial_file.html (serves to be includes, thus no need to have 'extends' but can use if needed)

- Function name/ method name: user camelcase: functionName

- Class name: captitalize first chars: ClassName

- Variable name: normal chars, separate by underscore:  var_name

- Boolean var: is_bool

CSS ---------------------------------------------------
- Id: use underscore: this_is_id
- Class: user tiret: this-is-class

Template ---------------------------------------------
- Block name: this-is-block-name