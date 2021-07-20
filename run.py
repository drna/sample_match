import optparse
from analysis.analysisManager import AnalysisManager
import sys

def get_options(args=None):
    optParser = optparse.OptionParser()
    optParser.add_option("-a", "--action", dest="action",
                         help="defines what action to take (0 - List Saves; 1 - Load new data; 2 - Output Matches; 3 - Output Metrics; 4 - Create new Save) (mandatory)")
    optParser.add_option("-s", "--save-name", dest="save_name",
                         help="defines the save-name (mandatory for all options but 0)")
    optParser.add_option("-d", "--data", dest="new_data",
                         help="New data csv filepath (mandatory for option 1)")

    (options, args) = optParser.parse_args(args=args)
    if not options.action:
        optParser.print_help()
        sys.exit(1)
    
    if int(options.action) not in range(5):
        print("Error, unknown action (-a, --action) must be 0, 1, 2, 3 or 4")
        optParser.print_help()
        sys.exit(1)
    else:
        options.action = int(options.action)
    
    if options.action != 0 and not options.save_name:
        print("Error, save name required (-s, --save_name)")
        optParser.print_help()
        sys.exit(1)

    if options.action == 1 and not options.new_data:
        print("Error, new data file required (-s, --save-name)")
        optParser.print_help()
        sys.exit(1)

    return options


def main(options):

    analysis_manager = AnalysisManager(options.save_name)

    if options.action == 0:
        print("Printing Saves")
        print(analysis_manager.list_save_names())
        pass
    if options.action == 1:
        print("Loading data")
        print(analysis_manager.load_save_file(options.new_data))
        pass
    if options.action == 2:
        print("Output Matches")
        print(analysis_manager.output_matches())
        pass
    if options.action == 3:
        print("Output Metrics")
        print(analysis_manager.output_metrics())
        pass
    if options.action == 4:
        print("Creating a new save")
        print(analysis_manager.create_save())
        pass

if __name__ == "__main__":
    if not main(get_options()):
        sys.exit(1)
