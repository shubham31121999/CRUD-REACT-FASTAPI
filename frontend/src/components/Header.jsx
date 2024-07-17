import React from "react";
import {Heading, Flex, Divider} from "@chakra-ui/react";

const Header = () => {
    return(
        <Flex
            as = "nav"
            align= "center"
            justify="space-between"
            wrap="wrap"
            paddingX  = "1rem"
            paddingY  = "1rem"
            bg = "twitter.500"
            color = "white"
            boxShadow = "0px 2px 4px rgba(0,0,0,0.2)">

            <Flex align = "center" ar={5}>
                <Heading as =  "h2"
                size ="lg"
                fontWeight="Bold">
                    TODO

                </Heading>

            </Flex>
        </Flex>
    )
};

export default Header;