// this is the three boxes lol

import React from 'react';
import { Box, Flex } from '@chakra-ui/react';


function Boxes({ result1, result2, result3 }) {
    return (
        <>
            {/* <CSSReset /> */}
            <Flex
                direction="row"
                w="100%" // Set the width to 100% to make it fill the page horizontally
                h="60vh" // Set the height of the container to 100vh for the entire viewport height
                bg="teal.50"
            >
                <Box
                    flex="1" // Let this box fill the available vertical space (bottom half)
                    bg="teal.500" // Background color for demonstration
                    mx={2}
                >
                    {result1}
                </Box>
                <Box
                    flex="1" // Each box within the flex container will fill the horizontal space evenly
                    bg="green.200" // Background color for demonstration
                    mx={2}
                >
                    {result2}
                </Box>
                <Box
                    flex="1" // Each box within the flex container will fill the horizontal space evenly
                    bg="red.200" // Background color for demonstration
                    mx={2}
                >
                    {result3}
                </Box>
            </Flex>
        </>
    );
}

export default Boxes;
