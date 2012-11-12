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

Environement -----------------------------------------
- Each environnement has its setting file: Production: PROD, Developpement: DEV
- This config is done in manage.py and fvresta.fcgi

When run if PROD via fastCGI, the config  will be charged with DJANGO_SETTINGS_MODULE = settings.prod
