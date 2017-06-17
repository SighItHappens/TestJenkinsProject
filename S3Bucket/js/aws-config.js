// WARNING: DO NOT EDIT. This file is Auto-Generated by AWS Mobile Hub. It will be overwritten.

// Copyright 2017 Amazon.com, Inc. or its affiliates (Amazon). All Rights Reserved.
// Code generated by AWS Mobile Hub. Amazon gives unlimited permission to
// copy, distribute and modify it.

// AWS Mobile Hub Project Constants
const aws_bots = 'enable';
const aws_bots_config = '[{"name":"HackathonJenkinsRun","alias":"$LATEST","description":"","bot-template":"bot-import","commands-help":[],"region":"us-east-1"}]';
const aws_cognito_identity_pool_id = 'us-east-1:c1e2991c-e42f-4a84-9488-1b1a7aee0f44';
const aws_cognito_region = 'us-east-1';
const aws_content_delivery = 'enable';
const aws_content_delivery_bucket = 'hackathonchatbot-hosting-mobilehub-147568170';
const aws_content_delivery_bucket_region = 'us-east-1';
const aws_content_delivery_cloudfront = 'enable';
const aws_content_delivery_cloudfront_domain = 'd2xbj91d0rh27w.cloudfront.net';
const aws_project_id = 'c1f99768-58cd-49ac-9873-00f0bd6f6db9';
const aws_project_name = 'HackathonChatBot';
const aws_project_region = 'us-east-1';
const aws_resource_name_prefix = 'hackathonchatbot-mobilehub-147568170';
const aws_sign_in_enabled = 'enable';
const aws_user_pools = 'enable';
const aws_user_pools_id = 'us-east-1_85xAnq0c1';
const aws_user_pools_mfa_type = 'OFF';
const aws_user_pools_web_client_id = '5lhe35l498ln30iuj370s32vqb';

AWS.config.region = aws_project_region;
AWS.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: aws_cognito_identity_pool_id
  }, {
    region: aws_cognito_region
});
AWS.config.update({customUserAgent: 'MobileHub v0.1'});