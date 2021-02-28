import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.escape_characters.py as escape_characters
import basics.output.ascii_art.py as ascii
import basics.input.user_input.py as user_input
import basics.input.ascii_robot.py as ascii_robot
import basics.input.data_types.py as data_types
import basics.input.review.py as review
import basics.input.string_operators.py as string_operators
import basics.decisions.simple_decision.comparison_operators.py as comparation_operator
import basics.decisions.simple_decision.counter.py as counter
import basics.decisions.simple_decision.if_elif_else.py as if_elif_else
import basics.decisions.simple_decision.if_else.py as if_else
import basics.decisions.simple_decision.modulo_operator.py as modulo_operator
import basics.decisions.simple_decision.nestception.py as nestception
import basics.decisions.simple_decision.nested.py as nested
import basics.decisions.and_operator.py as and_operator
import basics.decisions.or_operator.py as or_operator
import basics.decisions.review.py as deci_review
import basics.guess_the_number.py as guess
import basics.functions.ascii_ch.py as ascii_ch
import basics.functions.ascii_code.py as ascii_code
import basics.functions.function_with_loop.py as func_loop
import basics.functions.function_with_nesting.py as func_nesting
import basics.functions.function_with_parameter.py as func_parameter
import basics.functions.function_with_parameters.py as func_parameters
import basics.functions.function_calls.py as func_calls
import basics.functions.multiple_function.py as multi_func
import basics.functions.return_values.py as rtn_val
import basics.functions.simple_function.py as smpl_func





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
    elif (response == "if_py"):
        if_py.run()
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



def run():
    is_running = True

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
