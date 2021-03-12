
import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.escape_characters as escape_characters
import basics.output.ascii_art as ascii
import basics.input.user_input as user_input
import basics.input.ascii_robot as ascii_robot
import basics.input.data_types as data_types
import basics.input.review as review
import basics.input.string_operators as string_operators
import basics.decisions.simple_decision.comparison_operators as comparation_operator
import basics.decisions.simple_decision.counter as counter
import basics.decisions.simple_decision.if_elif_else as if_elif_else
import basics.decisions.simple_decision.if_else as if_else
import basics.decisions.simple_decision.modulo_operator as modulo_operator
import basics.decisions.simple_decision.nestception.py as nestception
import basics.decisions.simple_decision.nested as nested
import basics.decisions.and_operator as and_operator
import basics.decisions.or_operator as or_operator
import basics.decisions.review.py as deci_review
import basics.guess_the_number.py as guess
import basics.functions.ascii_ch as ascii_ch
import basics.functions.ascii_code as ascii_code
import basics.functions.function_with_loop as func_loop
import basics.functions.function_with_nesting as func_nesting
import basics.functions.function_with_parameter as func_parameter
import basics.functions.function_with_parameters as func_parameters
import basics.functions.function_calls as func_calls
import basics.functions.multiple_function as multi_func
import basics.functions.return_values as rtn_val
import basics.functions.simple_function as smpl_func
import basics.decisions.simple_decision as if_




def run_block_a():
    print("Which program in 'Block A: Basics' do you wish to run?")
    response = input()
    if (response == "simple_message"):
        simple_message.run()
    elif (response == "multiline_message"):
        multiline_message.run()
    elif (response == "escape_characters"):
        escape_characters.run()
    elif (response == "ascii"):
        ascii.run()
    elif (response == "user_input"):
        user_input.run()
    elif (response == "ascii_robot"):
        ascii_robot.run()
    elif (response == "data_types"):
        data_types.run()
    elif (response == "review"):
        review.run()
    elif (response == "string_operators"):
        string_operators.run()
    elif (response == "comparation_operator"):
        comparation_operator.run()
    elif (response == "counter"):
        counter.run()
    elif (response == "if_elif_else"):
        if_elif_else.run()
    elif (response == "if_"):
        if_.run()
    elif (response == "modulo_operator"):
        modulo_operator.run()
    elif (response == "nestception"):
        nestception.run()
    elif (response == "nested"):
        nested.run()
    elif (response == "and_operator"):
        and_operator.run()
    elif (response == "or_operator"):
        or_operator.run()
    elif (response == "deci_review"):
        deci_review.run()
    elif (response == "guess"):
        guess.run()
    elif (response == "ascii_ch"):
        ascii_ch.run()
    elif (response == "ascii_code"):
        ascii_code.run()
    elif (response == "func_loop"):
        func_loop.run()
    elif (response == "func_nesting"):
        func_nesting.run()
    elif (response == "func_parameter"):
        func_parameter.run()
    elif (response == "func_parameters"):
        func_parameters.run()
    elif (response == "func_calls"):
        func_calls.run()
    elif (response == "multi_func"):
        multi_func.run()
    elif (response == "rtn_val"):
        rtn_val.run()
    elif (response == "smpl_func"):
        smpl_func.run()
    elif (response == "if_else"):
        if_else.run()



def run():
    response = 0

    while (is_running):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if (response == "a"):
            run_block_a()
        elif (response == "q"):
            break
        else:
            print("Invalid option! Please try again.")


run()
