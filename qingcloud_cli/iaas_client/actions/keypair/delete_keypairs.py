# coding: utf-8

from qingcloud_cli.misc.utils import explode_array
from qingcloud_cli.iaas_client.actions.base import BaseAction

class DeleteKeyPairsAction(BaseAction):

    action = 'DeleteKeyPairs'
    command = 'delete-keypairs'
    usage = '%(prog)s -k keypair_id, ... [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-k', '--keypairs', dest='keypairs',
                action='store', type=str, default='',
                help='The comma separated IDs of keypairs you want to delete. ')
        
    @classmethod
    def build_directive(cls, options):
        keypairs = explode_array(options.keypairs)
        if not keypairs:
            return None
            
        return {'keypairs': keypairs}