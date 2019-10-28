from os.path import join, dirname

import settings

FILE_NAME_OF_LICENSE = settings.FILE_NAME_OF_LICENSE
FILE_DIRECTORY_OF_LICENSE = ".licenses"

def apply_licenses(eyetracker):
    print("------")
    license_file_path = join(dirname(__file__),  FILE_DIRECTORY_OF_LICENSE, FILE_NAME_OF_LICENSE)
    
    # <BeginExample>
    import tobii_research as tr

    print("Applying license from {0}.".format(license_file_path))
    with open(license_file_path, "rb") as f:
        license = f.read()

    failed_licenses_applied_as_list_of_keys = eyetracker.apply_licenses(
        [tr.LicenseKey(license)])
    failed_licenses_applied_as_list_of_bytes = eyetracker.apply_licenses([
                                                                         license])
    failed_licenses_applied_as_key = eyetracker.apply_licenses(
        tr.LicenseKey(license))
    failed_licenses_applied_as_bytes = eyetracker.apply_licenses(license)

    if len(failed_licenses_applied_as_list_of_keys) == 0:
        print("Successfully applied license from list of keys.")
    else:
        print("Failed to apply license from list of keys. Validation result: {0}.".
              format(failed_licenses_applied_as_list_of_keys[0].validation_result))

    if len(failed_licenses_applied_as_list_of_bytes) == 0:
        print("Successfully applied license from list of bytes.")
    else:
        print("Failed to apply license from list of bytes. Validation result: {0}.".
              format(failed_licenses_applied_as_list_of_bytes[0].validation_result))

    if len(failed_licenses_applied_as_key) == 0:
        print("Successfully applied license from single key.")
    else:
        print("Failed to apply license from single key. Validation result: {0}.".
              format(failed_licenses_applied_as_key[0].validation_result))

    if len(failed_licenses_applied_as_bytes) == 0:
        print("Successfully applied license from bytes object.")
    else:
        print("Failed to apply license from bytes object. Validation result: {0}.".
              format(failed_licenses_applied_as_bytes[0].validation_result))
    # <EndExample>
