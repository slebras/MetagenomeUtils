# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class MetagenomeUtils(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def file_to_binned_contigs(self, params, context=None):
        """
        file_to_binned_contigs: Generating BinnedContigs ojbect from files
        input params:
        file_directory: file directory containing compressed/unpacked contig file(s) to build BinnedContig object
        assembly_ref: Metagenome assembly object reference
        binned_contig_name: BinnedContig object name
        workspace_name: the name/id of the workspace it gets saved to
        return params:
        binned_contig_obj_ref: generated result BinnedContig object reference
        :param params: instance of type "FileToBinnedContigParams"
           (file_directory: file directory containing compressed/unpacked
           contig file(s) to build BinnedContig object assembly_ref:
           Metagenome assembly object reference binned_contig_name:
           BinnedContig object name workspace_name: the name/id of the
           workspace it gets saved to) -> structure: parameter
           "file_directory" of String, parameter "assembly_ref" of type
           "obj_ref" (An X/Y/Z style reference), parameter
           "binned_contig_name" of String, parameter "workspace_name" of
           String
        :returns: instance of type "FileToBinnedContigResult" -> structure:
           parameter "binned_contig_obj_ref" of type "obj_ref" (An X/Y/Z
           style reference)
        """
        return self._client.call_method(
            'MetagenomeUtils.file_to_binned_contigs',
            [params], self._service_ver, context)

    def binned_contigs_to_file(self, params, context=None):
        """
        binned_contigs_to_file: Convert BinnedContig object to fasta files and pack them to shock
        required params:
        input_ref: BinnedContig object reference
        optional params:
        not_save_to_shock: not saving result bin files to shock
        return params:
        shock_id: saved packed file shock id (None if not_save_to_shock is set)
        bin_file_list: a list of bin file path
        :param params: instance of type "ExportParams" (input_ref:
           BinnedContig object reference optional params: not_save_to_shock:
           not saving result bin files to shock) -> structure: parameter
           "input_ref" of String, parameter "not_save_to_shock" of type
           "boolean" (A boolean - 0 for false, 1 for true. @range (0, 1))
        :returns: instance of type "ExportOutput" (shock_id: saved packed
           file shock id bin_file_list: a list of bin file path) ->
           structure: parameter "shock_id" of String, parameter
           "bin_file_list" of list of String
        """
        return self._client.call_method(
            'MetagenomeUtils.binned_contigs_to_file',
            [params], self._service_ver, context)

    def extract_binned_contigs_as_assembly(self, params, context=None):
        """
        extract_binned_contigs_as_assembly: extract one/multiple Bins from BinnedContigs as Assembly object
        input params:
        binned_contig_obj_ref: BinnedContig object reference
        extracted_assemblies: a list of:
              bin_id: target bin id to be extracted
              output_assembly_name: output assembly object name
        workspace_name: the name of the workspace it gets saved to
        return params:
        assembly_ref_list: list of generated result Assembly object reference
        report_name: report name generated by KBaseReport
        report_ref: report reference generated by KBaseReport
        :param params: instance of type "ExtractBinAsAssemblyParams"
           (binned_contig_obj_ref: BinnedContig object reference
           extracted_assemblies: a list of: bin_id: target bin id to be
           extracted output_assembly_name: output assembly object name
           workspace_name: the name of the workspace it gets saved to) ->
           structure: parameter "binned_contig_obj_ref" of type "obj_ref" (An
           X/Y/Z style reference), parameter "bin_id" of String, parameter
           "output_assembly_name" of String, parameter "extracted_assemblies"
           of list of mapping from String to String, parameter
           "workspace_name" of String
        :returns: instance of type "ExtractBinAsAssemblyResult"
           (assembly_ref_list: list of generated Assembly object reference
           report_name: report name generated by KBaseReport report_ref:
           report reference generated by KBaseReport) -> structure: parameter
           "assembly_ref_list" of list of type "obj_ref" (An X/Y/Z style
           reference), parameter "report_name" of String, parameter
           "report_ref" of String
        """
        return self._client.call_method(
            'MetagenomeUtils.extract_binned_contigs_as_assembly',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('MetagenomeUtils.status',
                                        [], self._service_ver, context)
